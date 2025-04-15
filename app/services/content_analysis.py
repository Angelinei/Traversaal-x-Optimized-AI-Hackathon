from agentpro.core import Agent, Step

class ContentAuditAgent(Agent):
    def setup(self):
        self.add_step(Step(name="extract", func=self.extract_text))
        self.add_step(Step(name="analyze", func=self.analyze_content))
        self.add_step(Step(name="suggest", func=self.generate_suggestions))

    def extract_text(self, input_data):
        return {"text": input_data["file"].decode("utf-8")}

    def analyze_content(self, context):
        text = context["text"]
        return {"issues": ["Outdated module", "Missing reference to AI ethics"]}

    def generate_suggestions(self, context):
        issues = context["issues"]
        suggestions = [f"Update: {issue}" for issue in issues]
        return {"suggestions": suggestions}
