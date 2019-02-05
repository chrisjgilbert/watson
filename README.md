# Watson   

A Python module built using the IBM Watson SDK.

## How to set up   
* git clone this repo
* [Sign up for an api key here](https://cloud.ibm.com/apidocs/tone-analyzer) and save in ENV as `WATSON_TONE_ANALYZER`
* In project root `pip install --upgrade watson-developer-cloud`


## How to run
`python3 -i watson.py `   
```python
>>> tone_analyzer = ToneAnalyzer()
>>> tone_analyzer.send_for_analysis('i am super excited about today')
```
Example response:
```python
'{"document_tone": {"tones": [{"score": 0.926773, "tone_id": "joy", "tone_name": "Joy"}, {"score": 0.75152, "tone_id": "tentative", "tone_name": "Tentative"}]}}'
```
