from __future__ import annotations

from jewelry3d.engines.base import EngineContext


class ShapEEngine:
    name = "shap_e"

    def generate(self, prompt: str, out_path: str, ctx: EngineContext) -> str:
        # Import locale per evitare import pesanti quando non serve
        from src.shape_generate import generate_obj_with_shape

        generate_obj_with_shape(
            prompt=prompt,
            out_path=out_path,
            data=ctx.config,
            seed_offset=0,
        )
        return out_path
