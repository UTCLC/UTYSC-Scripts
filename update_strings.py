# By Gemini
import json
import time
import re
from collections import Counter, defaultdict
from difflib import SequenceMatcher

def process_json_merges(old_path, edited_path, new_path, output_path, fuzzy_log_path, missing_log_path):
    """
    高效地将编辑过的JSON字符串变更合并到新的JSON文件中，并生成详细的日志。

    - output.json: 最终合并成功的文件。
    - familiar.json: 所有通过近似（模糊）匹配完成的变更记录。
    - missing.json: 所有无法在目标文件中找到匹配项而被记录为缺失的变更。

    Args:
        old_path (str): 原始JSON文件的路径。
        edited_path (str): 已编辑的JSON文件的路径。
        new_path (str): 包含新内容的目标JSON文件的路径。
        output_path (str): 输出合并结果的JSON文件路径。
        fuzzy_log_path (str): 输出模糊匹配记录的JSON文件路径。
        missing_log_path (str): 输出缺失记录的JSON文件路径。
    """
    # --- 配置参数 ---
    SIMILARITY_THRESHOLD = 0.8
    CANDIDATE_LIMIT = 5
    CODE_PREFIXES = ["gml_", "spr_", "obj_", "graphic_", "base_", "rm_", "mus_", "mus/", "snd_", "snd/", "Tiles_"]

    # --- 1. 文件加载 ---
    try:
        print("正在加载 JSON 文件...")
        with open(old_path, 'r', encoding='utf-8') as f:
            old_j = json.load(f)["Strings"]
        with open(edited_path, 'r', encoding='utf-8') as f:
            edited_j = json.load(f)["Strings"]
        with open(new_path, 'r', encoding='utf-8') as f:
            new_j = json.load(f)["Strings"]
    except FileNotFoundError as e:
        print(f"错误: 文件未找到 - {e}")
        return
    except json.JSONDecodeError as e:
        print(f"错误: JSON 解析失败 - {e}")
        return

    start_time = time.time()
    result_j = list(new_j)
    
    # --- 2. 创建索引 ---
    print("正在为 new.json 创建快速查找索引...")
    new_string_to_index_exact = {string: i for i, string in enumerate(new_j)}
    
    token_to_indices_fuzzy = defaultdict(list)
    word_pattern = re.compile(r'\w+')
    for i, string in enumerate(new_j):
        tokens = set(word_pattern.findall(string.lower()))
        for token in tokens:
            token_to_indices_fuzzy[token].append(i)
    print("索引创建完成。")

    # --- 3. 合并变更 ---
    changed_count = 0
    used_target_indices = set()
    # 用于存储各种日志的字典
    fuzzy_matches_log = {}
    missing_log = {} # 已重命名

    print("开始处理变更...")
    for i, (old_string, edited_string) in enumerate(zip(old_j, edited_j)):
        if old_string == edited_string or any(old_string.startswith(p) for p in CODE_PREFIXES):
            continue

        target_index = -1
        is_fuzzy_match = False

        # 策略A: 精确匹配
        exact_match_index = new_string_to_index_exact.get(old_string)
        if exact_match_index is not None and exact_match_index not in used_target_indices:
            target_index = exact_match_index
        else:
            # 策略B: 模糊匹配
            is_fuzzy_match = True
            candidate_counter = Counter()
            old_tokens = set(word_pattern.findall(old_string.lower()))
            if not old_tokens:
                missing_log[str(i + 1)] = old_string
                continue

            candidate_indices = []
            for token in old_tokens:
                candidate_indices.extend(token_to_indices_fuzzy.get(token, []))
            candidate_counter = Counter(candidate_indices)
            
            best_match_index = -1
            highest_ratio = 0.0
            
            top_candidates = [
                (idx, count) for idx, count in candidate_counter.most_common(CANDIDATE_LIMIT * 5)
                if idx not in used_target_indices
            ][:CANDIDATE_LIMIT]
            
            for idx, _ in top_candidates:
                ratio = SequenceMatcher(None, old_string, new_j[idx]).ratio()
                if ratio > highest_ratio:
                    highest_ratio = ratio
                    best_match_index = idx
            
            if highest_ratio >= SIMILARITY_THRESHOLD:
                target_index = best_match_index
                key = str(i + 1)
                value = f"{old_string} : {new_j[target_index]} : {highest_ratio:.4f}"
                fuzzy_matches_log[key] = value

        if target_index != -1:
            match_type = "近似" if is_fuzzy_match else "精确"
            if result_j[target_index] != edited_string:
                print(f"应用变更 ({match_type}匹配): [源行 {i+1}] -> [目标行 {target_index+1}]")
                result_j[target_index] = edited_string
                changed_count += 1
            used_target_indices.add(target_index)
        else:
            # 记录未匹配上的变更到 missing_log
            missing_log[str(i + 1)] = old_string
            print(f"警告 [源行 {i+1}]: 在 new.json 中未找到 '{old_string}' 的匹配项。已记录为缺失。")

    # --- 4. 汇总与保存 ---
    print("\n---------- 合并报告 ----------")
    print(f"总共应用了 {changed_count} 处变更。")
    print(f" - 其中 {len(fuzzy_matches_log)} 处为近似匹配。")
    print(f"总共有 {len(missing_log)} 处变更因无法匹配而被记录为缺失。")
    print("---------------------------------")


    print(f"\n正在将合并结果写入 '{output_path}'...")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({"Strings": result_j}, f, indent=4, ensure_ascii=False)

    if fuzzy_matches_log:
        print(f"正在将 {len(fuzzy_matches_log)} 条近似匹配记录写入 '{fuzzy_log_path}'...")
        with open(fuzzy_log_path, 'w', encoding='utf-8') as f:
            json.dump(fuzzy_matches_log, f, indent=4, ensure_ascii=False, sort_keys=lambda k: int(k))
    else:
        print("没有检测到近似匹配，无需生成 familiar.json。")
    
    # 保存缺失的日志文件
    if missing_log:
        print(f"正在将 {len(missing_log)} 条缺失记录写入 '{missing_log_path}'...")
        with open(missing_log_path, 'w', encoding='utf-8') as f:
            json.dump(missing_log, f, indent=4, ensure_ascii=False, sort_keys=lambda k: int(k))
    else:
        print("所有变更均成功匹配，无需生成 missing.json。")

    end_time = time.time()
    print(f"\n操作成功完成！总耗时: {end_time - start_time:.2f} 秒。")

# --- 主程序入口 ---
if __name__ == '__main__':
    old_file_path = input("旧的 json 文件路径: ")
    edited_file_path = input("编辑后的 json 文件路径: ")
    new_file_path = input("新的 json 文件路径: ")
    
    # 定义所有输出文件的名称
    output_file_path = "output.json"
    fuzzy_log_file_path = "familiar.json"
    missing_log_file_path = "missing.json"

    process_json_merges(
        old_file_path,
        edited_file_path,
        new_file_path,
        output_file_path,
        fuzzy_log_file_path,
        missing_log_file_path
    )