import onnxruntime as ort


class PredictBase:

    def get_onnx_session(self, model_path, use_gpu=False):
        # Use GPU if requested and available
        if use_gpu:
            providers = ["CUDAExecutionProvider"]
        else:
            providers = ["CPUExecutionProvider"]
        # Create the ONNX inference session with the determined providers
        onnx_session = ort.InferenceSession(model_path, sess_options=None, providers=providers)

        return onnx_session

    def get_output_name(self, onnx_session):
        """
        output_name = onnx_session.get_outputs()[0].name
        :param onnx_session:
        :return:
        """
        output_name = []
        for node in onnx_session.get_outputs():
            output_name.append(node.name)
        return output_name

    def get_input_name(self, onnx_session):
        """
        input_name = onnx_session.get_inputs()[0].name
        :param onnx_session:
        :return:
        """
        input_name = []
        for node in onnx_session.get_inputs():
            input_name.append(node.name)
        return input_name

    def get_input_feed(self, input_name, image_numpy):
        """
        input_feed={self.input_name: image_numpy}
        :param input_name:
        :param image_numpy:
        :return:
        """
        input_feed = {}
        for name in input_name:
            input_feed[name] = image_numpy
        return input_feed
