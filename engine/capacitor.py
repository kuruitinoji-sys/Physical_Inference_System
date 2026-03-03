class EmotionCapacitor:
    def __init__(self, initial_q=0.5, gamma=0.8):
        self.q = initial_q
        self.gamma = gamma

    def update(self, eta: float) -> float:
        """
        電荷更新式 (Section 4.1): Q_{t+1} = (Q_t * gamma) + Q_{input}
        """
        q_input = eta * 0.2  # 粘性に比例したエネルギー入力
        q_new = (self.q * self.gamma) + q_input
        
        # 物理的クランプ (0.0 〜 1.0)
        self.q = max(0.0, min(q_new, 1.0))
        return self.q

    def ground(self):
        """完全接地 (Zero-Volt Check)"""
        self.q = 0.0

    def get_state(self) -> dict:
        return {
            "charge": round(self.q, 3),
            "mode": "Stable" if self.q < 0.8 else "HIGH_VOLTAGE"
        }

# セッション管理用のマネージャー
class CapacitorManager:
    def __init__(self):
        self.sessions: dict[str, EmotionCapacitor] = {}

    def get_session(self, session_id: str) -> EmotionCapacitor:
        if session_id not in self.sessions:
            self.sessions[session_id] = EmotionCapacitor()
        return self.sessions[session_id]
