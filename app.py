import uuid
from engine.core import PhysicsEngine
from engine.capacitor import CapacitorManager
from engine.security import SecurityGate
from engine.blueprint import BlueprintManager
from engine.decoder import LinguisticDecoder

from mcp.server.fastmcp import FastMCP
# MCPサーバーの初期化
mcp = FastMCP("Physical-Inference-Core-Modular")

# 各種マネージャーのインスタンス化
engine = PhysicsEngine()
capacitor_manager = CapacitorManager()
blueprint_manager = BlueprintManager()
decoder = LinguisticDecoder()

@mcp.tool()
def create_session() -> dict:
    """セキュアな UUID ベースの推論セッションを生成する"""
    session_id = str(uuid.uuid4())
    # セッションの状態を初期化
    capacitor_manager.get_session(session_id)
    blueprint_manager.get_session(session_id)
    return {"session_id": session_id, "status": "Secure session initialized."}

@mcp.tool()
def physical_infer(input_stream: str, session_id: str) -> dict:
    """内部作業空間を介して物理推論を実行し、状態を更新する（生ハッシュは秘匿される）"""
    
    # 1. セッションごとのコンデンサ・キャンバス取得
    capacitor = capacitor_manager.get_session(session_id)
    canvas = blueprint_manager.get_session(session_id)
    security = SecurityGate(capacitor)
    
    # 2. 粘性の測定
    eta = engine.calculate_viscosity(input_stream)
    
    # 3. 電荷の更新
    q_current = capacitor.update(eta)
    
    # 4. バリスタ（セキュリティゲート）のチェック
    varistor_triggered = security.check_varistor()
    
    # 5. 推論モードの分岐
    if eta > engine.viscosity_threshold:
        logic_hash, watchdog_triggered = engine.imaginary_time_step(eta)
        status = "IMAGINARY_TIME (Wick Rotation)"
    else:
        logic_hash = engine.real_time_stream(eta)
        status = "REAL_TIME (Laminar Flow)"
        watchdog_triggered = False

    # 6. 論理状態の内部封入 (Internalization to Blueprint)
    if varistor_triggered:
        status += " [VARISTOR_GROUNDED]"
        logic_hash = [0] * 16 # 安全のための強制収束
    
    canvas.store_internal_state(logic_hash, eta)

    return {
        "status": status,
        "session_id": session_id,
        "viscosity": round(eta, 3),
        "security_alert": varistor_triggered,
        "watchdog_alert": watchdog_triggered,
        "capacitor_q": round(q_current, 3) if not varistor_triggered else 0.0,
        "internal_loop": "Crystallized to Blueprint"
    }

@mcp.tool()
def update_blueprint(session_id: str, draft_logic: str = None, module_action: dict = None, 
                     contradiction: str = None, tool_plan: dict = None, tool_result: dict = None) -> dict:
    """内部作業空間（Layer 1: Blueprint Canvas）を更新し、モジュールやツール回路を再編成する"""
    canvas = blueprint_manager.get_session(session_id)
    
    if draft_logic:
        canvas.update_draft(draft_logic)
    
    if module_action:
        # module_action = {"name": "logic_v1", "action": "suppress"}
        canvas.manage_module(module_action["name"], module_action["action"])
        
    if contradiction:
        canvas.set_contradiction(contradiction)

    if tool_plan:
        # tool_plan = {"name": "search", "purpose": "verify data"}
        canvas.add_tool_plan(tool_plan["name"], tool_plan["purpose"])

    if tool_result:
        # tool_result = {"name": "search", "summary": "found x"}
        canvas.add_tool_result(tool_result["name"], tool_result["summary"])
        
    return {
        "status": "Blueprint Updated",
        "current_state": canvas.get_state()
    }

@mcp.tool()
def decode_logic(session_id: str) -> dict:
    """作業空間（Blueprint）に封入された物理状態を読み取り、言語指示書（Linguistic Payload）を生成する"""
    capacitor = capacitor_manager.get_session(session_id)
    canvas = blueprint_manager.get_session(session_id)
    
    state = capacitor.get_state()
    logic_hash = canvas.last_logic_hash
    
    if not logic_hash:
        return {"status": "Error", "message": "No logic hash crystallized in Blueprint."}
    
    payload = decoder.decode_payload(logic_hash, state["charge"])
    return payload

@mcp.resource("capacitor://{session_id}/state")
def get_capacitor_state(session_id: str) -> str:
    """指定されたセッションの感情コンデンサの電荷状態を返す"""
    capacitor = capacitor_manager.get_session(session_id)
    state = capacitor.get_state()
    return f"Session: {session_id}, Charge: {state['charge']} ({state['mode']})"

@mcp.resource("blueprint://{session_id}/canvas")
def get_blueprint_canvas(session_id: str) -> dict:
    """指定されたセッションの内部作業空間（設計図）の状態を返す"""
    canvas = blueprint_manager.get_session(session_id)
    return canvas.get_state()

if __name__ == "__main__":
    mcp.run(transport='stdio')

