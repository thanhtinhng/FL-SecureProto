import flwr as fl
import ssl

# Cấu hình SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain("certs/server.crt", "certs/server.key")

# Khởi chạy server Flower với SSL
fl.server.start_server(
    server_address="0.0.0.0:8080",
    config=fl.server.ServerConfig(num_rounds=3),
    ssl_context=context
)