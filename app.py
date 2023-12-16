from flask import Flask,request
from gemeni_model import Model
from langchain.document_loaders import YoutubeLoader

app=Flask(__name__)

@app.route('/summarize',methods=['GET','POST'])
def api():
    try:
      url=request.args.get('url','')
      summary=Model.model(text=get_transcipt(url))
      return summary,200
    except Exception as e:
        return "Not able to summarize this video...."
  
def get_transcipt(url):
    loader=YoutubeLoader.from_youtube_url(url,add_video_info=True)
    text=loader.load()
    return text[0].page_content
    
if __name__=='__main__':
    app.run()

