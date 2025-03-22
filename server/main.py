# import flwr as fl
# import ssl

# # Cấu hình SSL
# context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# context.load_cert_chain("certs/server.crt", "certs/server.key")

# # Khởi chạy server Flower với SSL
# fl.server.start_server(
#     server_address="0.0.0.0:8080",
#     config=fl.server.ServerConfig(num_rounds=3),
#     ssl_context=context
# )

# import flwr as fl

# # Định nghĩa chiến lược huấn luyện
# strategy = fl.server.strategy.FedAvg(  # Có thể thay bằng chiến lược khác
#     fraction_fit=0.5,  # 50% client tham gia mỗi vòng
#     min_fit_clients=2,
#     min_available_clients=3,
#     num_rounds=3
# )

# # Khởi động server Flower với SuperLink
# fl.server.start_server(
#     server_address="0.0.0.0:9092",  # Địa chỉ của SuperNode
#     config=fl.server.ServerConfig(num_rounds=3),
#     strategy=strategy
# )
