# src/robot_hardening_sim/mqtt_check.py
import ssl, socket

def check_mqtt_tls(host: str, port: int = 8883, timeout: float = 3.0) -> bool:
    """
    Returns True if a TLS handshake succeeds to the MQTT broker (default 8883), else False.
    """
    ctx = ssl.create_default_context()
    try:
        with ctx.wrap_socket(socket.socket(), server_hostname=host) as s:
            s.settimeout(timeout)
            s.connect((host, port))
            return True
    except Exception:
        return False
