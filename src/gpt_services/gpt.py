from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

class GPT2FlaskApp:
    def __init__(self, model_name="openai-community/gpt2", device=-1):
        """
        Initialize GPT-2 model and tokenizer.
        """
        self.model_name = model_name
        self.device = device
        self._load_model()

    def _load_model(self):
        """
        Load GPT-2 model and text-generation pipeline.
        """
        try:
            print(f"Loading model '{self.model_name}'...")
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
            self.generator = pipeline(
                "text-generation",
                model=self.model,
                tokenizer=self.tokenizer,
                device=self.device
            )
            print("✅ Model loaded successfully!")
        except Exception as e:
            print(f"Exception Error _load_model : {e}")

    def generate_text(self, prompt, max_new_tokens=400 ,num_return_sequences=1,pad_token_id=50256):
     
        try:

            outputs = self.generator(
                prompt,
                max_new_tokens=max_new_tokens,
                num_return_sequences=num_return_sequences,
                truncation=True,pad_token_id=pad_token_id
            )
            print(outputs)
            return [o["generated_text"] for o in outputs]
        except Exception as e:
            print(f"Exception Error  generate_text : {e}")

    def generate_cv_entry(self, name, age, location, skills, job_title, max_new_tokens=400,pad_token_id=50256):
        """
        Generate a professional CV summary for a given person.
        """
        try:
            print("This One  ************************************************************************************")
    
            new_prom = f"""
Below is an example of a professional CV summary.

Example:
[Input]: 
Name: Alice Smith
Age: 28
Location: Amman
Skills: Web Development, JavaScript, React
Job Title: Software Engineer

[Output]: 
Alice Smith is a Software Engineer specializing in web development using JavaScript and React.
She has experience building scalable, user-friendly web applications and collaborating across teams 
to deliver high-quality solutions.

Now, generate a professional CV summary for the following person:

[Input]: 
Name: {name}
Age: {age}
Location: {location}
Skills: {skills}
Job Title: {job_title}

[Output]:
"""

            
            generated = self.generate_text(new_prom, max_new_tokens=max_new_tokens, num_return_sequences=1,pad_token_id=50256)

            print("****"*50)
            output_text = generated[0].split("[Output]:")[-1].strip()
            print(output_text)
            
            return output_text
        except Exception as e:
            print(f"Exception Error generate_cv_entry : {e}")
