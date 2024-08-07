from pixellib.torchbackend.instance import instanceSegmentation

ins = instanceSegmentation()
ins.load_model("pointrend_resnet50.pkl")
ins.process_video("input.mp4", show_bboxes=True, frames_per_second=3, output_video_name="output.mp4")
