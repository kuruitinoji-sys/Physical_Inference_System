import pytest
import time

def test_system_flow():
    print("Testing Modular Physical Inference System (Hardened)...")
    
    from engine.core import PhysicsEngine
    from engine.capacitor import CapacitorManager
    from engine.security import SecurityGate
    from engine.blueprint import BlueprintManager
    from engine.decoder import LinguisticDecoder

    print("Testing Modular Physical Inference System (Hardened)...")
    
    from engine.core import PhysicsEngine
    from engine.capacitor import CapacitorManager
    from engine.security import SecurityGate
    from engine.blueprint import BlueprintManager
    from engine.decoder import LinguisticDecoder

    cm = CapacitorManager()
    engine = PhysicsEngine(watchdog_limit=1.0) # テスト用に制限をきつくする
    bm = BlueprintManager()
    dec = LinguisticDecoder()
    
    print("\n[Test 1] Session Isolation")
    cap1 = cm.get_session("user_a")
    cap2 = cm.get_session("user_b")
    cap1.update(0.9)
    print(f"User A Charge: {cap1.q}")
    print(f"User B Charge: {cap2.q}")
    assert cap1.q != cap2.q

    print("\n[Test 2] Emotional Varistor (Grounding)")
    for _ in range(10):
        cap1.update(1.0)
    print(f"Charge before Varistor: {cap1.q}")
    gate = SecurityGate(cap1)
    triggered = gate.check_varistor()
    print(f"Varistor Triggered: {triggered}")
    print(f"Charge after Varistor: {cap1.q}")
    assert triggered == True
    assert cap1.q == 0.0

    print("\n[Test 3] Watchdog (Timeout)")
    # 粘性1.0なら 1.0 * 2.0 = 2.0s。limit 1.0s なので確実にタイムアウト
    logic, timeout = engine.imaginary_time_step(1.0)
    print(f"Watchdog Triggered: {timeout}")
    print(f"Internal Flux Vector (Length): {len(logic)}")
    assert timeout == True
    assert logic == [0] * 16

    print("\n[Test 4] Internalization & Blueprint (Layer 1)")
    canvas = bm.get_session("user_c")
    canvas.update_draft("Secure reasoning architecture")
    flux_vector = [1] * 16
    canvas.store_internal_state(flux_vector, 0.4)
    state = canvas.get_state()
    print(f"Blueprint State: {state}")
    assert canvas.last_logic_hash == flux_vector
    assert state["tool_results_count"] == 0

    print("\n[Test 5] Linguistic Decoder (Layer 2) - Closed Loop")
    # Blueprintに保存された高次元フラックスからガイダンスを生成
    payload = dec.decode_payload(canvas.last_logic_hash, 0.8)
    print(f"Linguistic Payload Summary: {payload['status']}")
    print(f"Output Guidance: {payload['output_guidance']}")
    # [1]*16 なら 振幅1.0 なので確信度は最大
    assert payload["linguistic_parameters"]["certainty_index"] == 1.0
    assert "断定的な口調" in payload["output_guidance"]

    print("\nAll tests passed successfully!")

if __name__ == "__main__":
    run_test()
