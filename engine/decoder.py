import math

class LinguisticDecoder:
    def __init__(self):
        self.tone_presets = {
            "analytic": {"stiffness": 0.8, "fluidity": 0.2},
            "empathic": {"stiffness": 0.3, "fluidity": 0.7},
            "neutral": {"stiffness": 0.5, "fluidity": 0.5}
        }

    def map_logic(self, logic_hash: list) -> dict:
        """論理ハッシュから確信度と言語剛性を算出する"""
        # ハッシュの総和から「安定性」を簡易評価
        # [1, 1, -1] -> 1/3, [1, 1, 1] -> 1.0 など
        if not logic_hash or len(logic_hash) == 0:
            return {"certainty": 0.5, "stiffness": 0.5}
            
        amplitude = sum(logic_hash) / len(logic_hash)
        certainty = abs(amplitude)
        
        # 剛性（stiffness）はハッシュの極性に依存
        stiffness = 0.5 + (amplitude * 0.3)
        
        return {
            "certainty": round(certainty, 3),
            "stiffness": round(stiffness, 3),
            "recommended_tone": "analytic" if certainty > 0.6 else "neutral"
        }

    def map_emotion(self, q: float) -> dict:
        """電荷 Q から感情ゲインと流動性を算出する"""
        # Qが0.95に近いほど「励起状態」
        gain = q * 1.5 # 1.0を超えると「過剰な熱量」
        fluidity = math.sin(q * math.pi / 2) # Qに比例して柔軟になる
        
        return {
            "energy_gain": round(gain, 3),
            "fluidity": round(fluidity, 3),
            "affective_intensity": "HIGH" if gain > 0.8 else "NORMAL"
        }

    def decode_payload(self, logic_hash: list, q: float) -> dict:
        """物理状態を包括的な言語指示書に射影する"""
        logic_map = self.map_logic(logic_hash)
        emotion_map = self.map_emotion(q)
        
        return {
            "status": "Crystallized",
            "linguistic_parameters": {
                "certainty_index": logic_map["certainty"],
                "tone_stiffness": logic_map["stiffness"],
                "energy_gain": emotion_map["energy_gain"],
                "context_fluidity": emotion_map["fluidity"],
                "affective_intensity": emotion_map["affective_intensity"]
            },
            "output_guidance": self._generate_guidance(logic_map, emotion_map)
        }

    def _generate_guidance(self, logic: dict, emotion: dict) -> str:
        guidance = []
        if logic["certainty"] > 0.7:
            guidance.append("断定的な口調を採用し、論理的根拠を強調せよ。")
        if emotion["energy_gain"] > 0.8:
            guidance.append("情動的な共感や熱意を言葉に込めよ。")
        if logic["stiffness"] > 0.7:
            guidance.append("専門用語を適切に使い、構造的な回答を心がけよ。")
        
        return " ".join(guidance) if guidance else "標準的なトーンで丁寧に回答せよ。"
