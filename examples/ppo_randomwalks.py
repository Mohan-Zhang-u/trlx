from randomwalks import generate_random_walks

import trlx
from trlx.data.configs import TRLConfig

if __name__ == "__main__":
    walks, logit_mask, metric_fn, eval_prompts = generate_random_walks(seed=1000)
    lengths = metric_fn(walks)["lengths"]

    config = TRLConfig.load_yaml("configs/ppo_randomwalks.yml")

    trlx.train(
        "randomwalks/1M",
        reward_fn=lambda xs: metric_fn(xs)["lengths"],
        eval_prompts=eval_prompts,
        metric_fn=metric_fn,
        config=config,
    )
