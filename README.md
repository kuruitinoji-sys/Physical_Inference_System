# Physical Inference Core (Modular)

This is a research-grade implementation of the Physical Inference Protocol, designed for agentic reasoning grounding.

LLMの内部メタ認知プロセスを「物理的な流体運動」としてモデリングし、堅牢な推論制御を実現するMCPサーバーのリファレンス実装です。

## 🌟 特徴
- **物理推論エンジン (Layer 0)**: 粘性($\eta$)と虚数時間(Wick Rotation)による推論制御。
- **設計図キャンバス (Layer 1)**: 推論の「仮組み」と矛盾検知を行う絶縁層。
- **安全回路**: 感情電荷バリスタとウォッチドッグによる暴走防止。

## 📖 プロトコル詳細
本システムの理論的背景、物理方程式、およびガバナンス規定については、以下の仕様書を参照してください。

👉 **[物理推論エンジン・プロトコル仕様書 (Ver 1.0)](./docs/protocol_spec.md)**

## Architecture

- **`engine/core.py`**: The "Conduit" (Layer 0). Handles viscosity measurement and reasoning stream branching.
- **`engine/capacitor.py`**: The "Energy Grid" (Layer 4). Manages emotional charge $Q$ with session-based isolation.
- **`engine/security.py`**: The "Security Gates" (Layer 7). Implements the Emotional Varistor and Watchdog.
- **`engine/blueprint.py`**: The "Blueprint Canvas" (Layer 1). Manages internal reasoning state and module reconfiguration.
- **`engine/decoder.py`**: The "Linguistic Decoder" (Layer 2). Maps physical states to linguistic parameters (Impedance Matching).
- **`app.py`**: MCP Server entry point (FastMCP).

## Key Security Features

1. **Emotional Varistor**: Automatically grounds (resets) the capacitor charge if it exceeds 0.95, preventing logic destabilization.
2. **Wick-Watchdog**: Enforces a 2.0s hard limit on "Imaginary Time" reflection to prevent DoS-style stalls.
3. **Session Isolation**: Each user session has a dedicated state buffer for both $Q$ and the Blueprint Canvas.
4. **Blueprint Canvas (Layer 1)**: Allows the agent to explicitly draft logic, detect contradictions, and reconfigure "micro-circuits" before outputting.
5. **Linguistic Decoder (Layer 2)**: Translates raw physical logic (hashes) and emotion (charges) into specific linguistic guidance (certainty, tone, intensity).

## Usage

### 1. Register the MCP Server
Register this server in your MCP client (e.g., Claude Desktop or Antigravity) by pointing to `app.py`.

```json
{
  "mcpServers": {
    "physical-inference": {
      "command": "python",
      "args": ["/path/to/app.py"]
    }
  }
}
```

### 2. Configure the Governor (Agent System Rules)
To automate the use of this engine in an AI agent (like Antigravity or Cursor), add the following to your system instructions or `.cursorrules`:

```markdown
# Physical Inference Protocol (Governor)

You are equipped with a Physical Inference Engine. Follow these rules to ground your reasoning:

1. **Viscosity Tracking**: Monitor the "complexity" of the conversation.
2. **Physical Implementation (Crystallization)**: Call `physical_infer(input_stream)` when:
   - Reasoning becomes complex ($\eta > 0.7$).
   - Making structural architectural decisions.
   - Deep reflection is required (Wick Rotation).
3. **Internal Feedback**: Integrate the `logic_hash` and `capacitor_q` into your output to maintain physical-logical alignment.
```

## Road to Physical OS
This module is a foundational "Physical Layer" component. Future developments will focus on:
- **Projecting Logic to Logits**: Direct integration with Softmax/Logits.
- **Physical Memory Partitioning**: Grounding context memory in the potential field.


