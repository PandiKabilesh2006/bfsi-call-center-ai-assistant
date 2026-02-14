
from transformers import pipeline,AutoModelForCausalLM,AutoTokenizer
import torch

class LocalSLM:
    def __init__(self):
        model_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
        self.tokenizer=AutoTokenizer.from_pretrained(model_name)
        self.model=AutoModelForCausalLM.from_pretrained(model_name)
        self.model.eval()
    def generate_response(self, query):
        system_prompt=(
            "You are a professional BFSI call center AI assistant.\n"
            "Follow strict financial compliance rules.\n"
            "Never guess financial numbers.\n"
            "Do not expose sensitive customer data.\n"
            "If unsure, advise contacting official support.\n\n"
            "Provide a clear, concise, professional answer.\n"
            "Do not continue conversation beyond one response.\n\n"
        )
        messages=[
            {"role":"system","content":system_prompt},
            {"role":"user","content":query}
        ]
        input_ids=self.tokenizer.apply_chat_template(
            messages,
            return_tensors="pt"
        )
        with torch.no_grad():
            output_ids=self.model.generate(
                input_ids,
                max_new_tokens=200,
                do_samples=False
            )
        generated_text=self.tokenizer.decode(
            output_ids[0],
            skip_special_tokens=True
        )
        if("assistant" in generated_text.lower()):
            response=generated_text.split("assistant"[-1]).strip()
        else:
            response=generated_text.strip()
        return response
        # final_prompt=system_prompt+"User Query: " +query+"\nAssistant:"
        # inputs=self.tokenizer(final_prompt,return_tensors="pt")
        # outputs=self.model.generate(
        #     **inputs,
        #     max_new_tokens=200,
        #     do_sample=False,
        #     eos_token_id=self.tokenizer.eos_token_id
        # )
        # generated_text=self.tokenizer.decode(outputs[0],skip_special_tokens=True)
        # response=generated_text.split("Assistant:")[-1].strip()
        # if("User:" in response):
        #     response=response.split("User:")[0].strip()
        # return response
