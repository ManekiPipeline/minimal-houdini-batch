import hou

# hip読み込み
root_directory = hou.text.expandString("$HIP")  # シーンを開く前はパス変数$HIPでlaunch.batのパスを取得します
hip_name = "pipeline.hip"
hip_path = f"{root_directory}/hip/{hip_name}"
hou.hipFile.load(hip_path)
print(f"hipを読み込ました: {hip_path}")

# TOP実行
top_path = "/obj/topnet1"
top_node = hou.node(top_path)
to_cook = top_node.displayNode()
print(f"{top_node} のクックを開始しました")
to_cook.cookWorkItems(block=True)
print(u"すべてのワークが完了しました")