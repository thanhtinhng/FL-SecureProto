# import ssl
# import flwr as fl

# # Cấu hình SSL Client
# context = ssl.create_default_context()
# context.load_cert_chain("certs/client1.crt", "certs/client1.key")
# context.load_verify_locations("certs/server.crt")

# # Triển khai Client với Flower
# # Định nghĩa client sẽ tham gia vào quá trình học FL như thế nào
# class MalwareDetectionClient(fl.client.NumPyClient):
#     def get_parameters(self, config):
#         return [b"params_placeholder"]  # Không cần ML thực tế
    
#     def fit(self, parameters, config): # Nhận tham số mô hình từ server, huấn luyện mô hình cục bộ (trong thực tế)
#         return parameters, len(parameters) # Trả về tham số mới (ở đây chỉ giữ nguyên vì không thực hiện ML thực tế)
    
#     # Trong thực tế, bạn sẽ thay thế fit() bằng huấn luyện thực tế trên dữ liệu malware
    
#     def evaluate(self, parameters, config): # Đánh giá mô hình sau khi huấn luyện
#         return 0.0, len(parameters), {} # Trả về 0.0 làm giá trị lỗi (vì không có ML thực tế)
    
# # Kết nối client với server
# fl.client.start_numpy_client(
#     server_address="127.0.0.1:8080",
#     client=MalwareDetectionClient(),
#     root_certificates="certs/server.crt"
# )

# import flwr as fl

# # Định nghĩa Client tham gia học FL
# class MalwareDetectionClient(fl.client.NumPyClient):
#     def get_parameters(self, config):
#         return [b"params_placeholder"]  # Không thực hiện ML thực tế
    
#     def fit(self, parameters, config):
#         return parameters, len(parameters)  # Giữ nguyên tham số
    
#     def evaluate(self, parameters, config):
#         return 0.0, len(parameters), {}  # Trả về loss = 0.0 (không có đánh giá thực tế)

# # Kết nối Client với SuperNode
# fl.client.start_numpy_client(
#     server_address="127.0.0.1:9092",  # Kết nối tới SuperNode, KHÔNG phải server trực tiếp
#     client=MalwareDetectionClient(),
# )
