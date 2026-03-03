class SecurityGate:
    def __init__(self, capacitor):
        self.capacitor = capacitor

    def check_varistor(self) -> bool:
        """
        電荷バリスタ (Section 7.2):
        異常電圧（HIGH_VOLTAGE）を検知した場合、強制接地し、リセット信号を送る。
        """
        state = self.capacitor.get_state()
        if self.capacitor.q > 0.95:
            self.capacitor.ground()
            return True # バリスタ作動
        return False

    def verify_grounding(self) -> bool:
        """接地確認シーケンス (Section 7.4)"""
        return self.capacitor.q == 0.0
