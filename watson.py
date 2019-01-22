import json
from watson_developer_cloud import ToneAnalyzerV3

class ToneAnalyzer:

    def __init__(self):
        self.tone_analyzer = ToneAnalyzerV3(
            version='2017-09-21',
            iam_apikey='BdDsmJd471Ez1TtMrk3bFoQawd0ETZGwsGNo3aS7ZPCC',
            url= 'https://gateway-lon.watsonplatform.net/tone-analyzer/api'
        )

    def send_for_analysis(self, text):
        tone_analysis = self.tone_analyzer.tone(
            { 'text': text },
            'application/json',
        ).get_result()
        print(json.dumps(tone_analysis, indent=2))
