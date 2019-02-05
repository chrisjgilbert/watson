# Watson   

A Python module that returns sentiment analysis on a string using the IBM Watson SDK.

## How to set up   
* Clone this repo
* [Sign up for an IBM Developer Cloud Tony Anaylzer API Key](https://cloud.ibm.com/apidocs/tone-analyzer) and save in ENV as `WATSON_TONE_ANALYZER`
* In project root `pip3 install --upgrade watson-developer-cloud`

## How to run  
* In project root `python3 -i lib/watson.py`
* Then in python REPL:  
```python
>>> tone_analyzer = ToneAnalyzer()
>>> tone_analyzer.send_for_analysis('i am super excited about today')
```

## Example response   
```python
'{"document_tone": {"tones": [{"score": 0.926773, "tone_id": "joy", "tone_name": "Joy"}, {"score": 0.75152, "tone_id": "tentative", "tone_name": "Tentative"}]}}'
```
