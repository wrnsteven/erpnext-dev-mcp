import json
from copy import deepcopy

# 读取原文件
with open("framework_urls.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 初始化统计字段
data["completed"] = 0
data["pending"] = data["total"]   # total 保持不变
data["processing"] = 0
data["failed"] = 0

# 重置每个 url 条目
for url in data["urls"]:
    url["status"] = "pending"
    # 删除或重置处理相关的字段
    url.pop("processed_at", None)
    url.pop("retry_count", None)
    url.pop("error", None)
    # 如果你想保留这些字段但设为默认值，可以这样：
    # url["retry_count"] = 0
    # url["processed_at"] = ""

# 保存为新文件（建议不覆盖原文件，另存为 _init.json）
output_path = "framework_urls_init.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"初始化完成！新文件已保存为: {output_path}")
print(f"总共 {data['total']} 条 URL，状态全部为 pending")
