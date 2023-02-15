import argparse
from diffusers import LMSDiscreteScheduler
from japanese_stable_diffusion import JapaneseStableDiffusionPipeline


def main(args):
    MODEL_ID = "rinna/japanese-stable-diffusion"
    device = "cpu"

    scheduler = LMSDiscreteScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear", num_train_timesteps=1000)
    pipe = JapaneseStableDiffusionPipeline.from_pretrained(MODEL_ID, scheduler=scheduler, use_auth_token=True)
    pipe = pipe.to(device)
    
    prompt = args.text
    image = pipe(prompt, guidance_scale=7.5)["images"][0]  
        
    image.save(args.output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--text", type=str)
    parser.add_argument("--output", type=str)

    args, _ = parser.parse_known_args()

    main(args)
