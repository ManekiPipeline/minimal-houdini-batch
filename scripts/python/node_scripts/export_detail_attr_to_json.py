import os
import hou
import pdg
import json
import pathlib

node = hou.pwd()
geo = node.geometry()

# ワークアイテムを参照
item = pdg.workItem()

# topアトリビュートを取得し、出力パスを作成
source = item.attribValue("filename")
hip_root = hou.expandString("$HIP")
# project_rootのパス取得が判りにくい書き方になっているので実運用ではpackage等でパス変数を作ることをお勧めします
# シンプルな構造として用意するうえではわかりずらくなってしまうので今回packageは割愛しました
project_root = os.path.dirname(hip_root)
output_directory = pathlib.Path(f"{project_root}/output")
output_directory.mkdir(parents=True, exist_ok=True)
output_file = f"{output_directory}/{source}.json".replace(os.sep, "/")

# jsonに含めるアトリビュートを参照
extract_data = {}
for _detail_attr in geo.globalAttribs():
    attr_name = _detail_attr.name()
    detail_value = geo.attribValue(_detail_attr.name())
    extract_data[attr_name] = detail_value

# jsonとして出力
with open(output_file, "w") as f:
    json.dump(extract_data, f, indent=4)
