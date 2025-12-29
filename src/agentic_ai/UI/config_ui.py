from configparser import ConfigParser

class Config:
    def __init__(self, config_file_path = "src/agentic_ai/UI/config_ui.ini") -> None:
        self.config = ConfigParser()
        self.config.read(config_file_path)

    def get_llm_options(self):
        return [x.strip() for x in self.config["DEFAULT"]["LLM_OPTIONS"].split(",")]
    
    def get_usecase_options(self):
        return [x.strip() for x in self.config["DEFAULT"]["USECASE_OPTIONS"].split(",")]
    
    def get_groq_model_options(self):
        return [x.strip() for x in self.config["DEFAULT"]["GROQ_MODEL_OPTIONS"].split(",")]
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE","")
    
    