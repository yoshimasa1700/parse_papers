## parse_papers

This reposiroty contains easy script for parse pdf paper to markdown.

### setup

```shell
pip3 install git+https://github.com/titipata/scipdf_parser
pip3 install spacy
python3 -m spacy download en_core_web_sm
```


### run

```shell
bash serve_grobid.sh
python3 parse_papers.py [paper pdf] [output markdown]
```
