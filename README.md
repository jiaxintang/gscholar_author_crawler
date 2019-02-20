# gscholar_author_crawler

## Preparation

- Download the chromedriver corresponding to Chrome from ```https://chromedriver.storage.googleapis.com/index.html```, and put it in the project directory.

- The chromedriver version corresponding to Chrome is as follows：

| chromedriver | Chrome |
| ------ | ------ |
| v2.46 | v71-73 |
| v2.45 | v70-72 |
| v2.44 | v69-71 |
| v2.43 | v69-71 |
| v2.42 | v68-70 |
| v2.41 | v67-69 |
| v2.40 | v66-68 |
| v2.39 | v66-68 |
| v2.38 | v65-67 |
| v2.37 | v64-66 |
| v2.36 | v63-65 |
| v2.35 | v62-64 |
| v2.34 | v61-63 |
| v2.33 | v60-62 |
| v2.32 | v59-61 |
| v2.31 | v58-60 |
| v2.30 | v58-60 |

- The version of Chrome can be found from ```chrome://settings/help``` or the command ```google-chrome --version```

## Run
	python main.py

## Description
+ The url of author's profile (author_url_list) is stored in a redis server which is build on 184.170.214.178.
+ The author's unique id which has been crawler or is going to be crawler (stored in author_url_list) is also stored in the redis server. 
+ Each time the crawel meet a new author, it will push it into author_url_list.
+ The results of the crawler is stored in the author_list directory under the project. 



