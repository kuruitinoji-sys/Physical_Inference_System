class BlueprintCanvas:
    def __init__(self):
        self.draft_logic = ""
        self.active_modules = set(["core_reasoning"])
        self.suppressed_modules = set()
        self._contradiction_flags = [] # システム専用 (Locked)
        self.planned_tools = []
        self.tool_results = {}
        self._last_logic_hash = [] # システム専用 (Locked)
        self.last_viscosity = 0.0

    def update_draft(self, text: str):
        """設計図（思考の仮組み）を更新する。エージェントはここを自由に変更可能。"""
        self.draft_logic = text

    def manage_module(self, module_name: str, action: str):
        """マイクロ回路の動的再構成。エージェントの意図による構成変更。"""
        if action == "activate":
            self.active_modules.add(module_name)
            self.suppressed_modules.discard(module_name)
        elif action == "suppress":
            self.suppressed_modules.add(module_name)
            self.active_modules.discard(module_name)

    def set_contradiction(self, description: str):
        """矛盾検知フラグの記録。エージェント側からは追加のみ許可（削除は不可）。"""
        self._contradiction_flags.append(f"[AGENT_REPORT] {description}")

    def clear_canvas(self):
        """設計図の初期化。エージェントが書き換え可能なもののみ初期化可能。"""
        self.draft_logic = ""
        # 矛盾フラグは証跡として保護する

    def store_internal_state(self, logic_hash: list, viscosity: float):
        """物理コア出力を内部作業空間に封入する (System Only / Read-Only for Agent)"""
        self._last_logic_hash = logic_hash
        self.last_viscosity = viscosity

    @property
    def last_logic_hash(self):
        return self._last_logic_hash

    @property
    def contradiction_flags(self):
        return self._contradiction_flags

    def add_tool_plan(self, tool_name: str, purpose: str):
        """ツールの実行を予約する"""
        self.planned_tools.append({"name": tool_name, "purpose": purpose})

    def add_tool_result(self, tool_name: str, summary: str):
        """ツールの実行結果（要約）を記録する"""
        self.tool_results[tool_name] = summary

    def get_state(self) -> dict:
        return {
            "draft_logic_preview": self.draft_logic[:100] + ("..." if len(self.draft_logic) > 100 else ""),
            "active_modules": list(self.active_modules),
            "suppressed_modules": list(self.suppressed_modules),
            "contradiction_count": len(self._contradiction_flags),
            "planned_tools": self.planned_tools,
            "tool_results_count": len(self.tool_results)
        }

class BlueprintManager:
    def __init__(self):
        self.sessions: dict[str, BlueprintCanvas] = {}

    def get_session(self, session_id: str) -> BlueprintCanvas:
        if session_id not in self.sessions:
            self.sessions[session_id] = BlueprintCanvas()
        return self.sessions[session_id]
