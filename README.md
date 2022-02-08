# Automatic Question Generation & Difficulty Control for the Portuguese Language

<img src="images/webapp_1.jpg" style="width: 15%; height: 15%" align="right" />

## Overview
We present a **tool** capable of automatically **generating questions in Portuguese** with **controlled difficulty**. Our methodology is guided by three different kinds of questions: (A) Grammar, (B) Factoid (*wh-questions*), and (C) Pronoun reference. For the former (A), we have followed a rule-based approach by establishing rules aligned with the Portuguese grammar. For reading comprehension (B), we generate facoid (who-type) questions and, for that, we tested five different methods. The first one performs a syntax-based analysis by using the information obtained from Part-of- speech tagging and Named Entity Recognition. The second carries out a semantic analysis of the sentences, through Semantic Role Labeling. The third method extracts the inherent dependencies within sentences using Dependency Parsing. The fourth takes advantage of the relative pronouns and adverbs found in the sentences. The fifth explores the usefulness and practicality of discourse connectors. Finally, for the last approach (C), we create pronoun reference questions, in which we do not only generate our questions but also the text excerpts they are generated from. We define heuristic functions that assign difficulty values for each question.

## Main Features
* Factoid Question Generation
* Grammar Question Generation
* Pronoun Reference Question Generation
* Difficulty Controllable

## Prerequisites
```bash
Python 3
Java
```

## Installation
1. Install the Python packages from [requirements.txt](https://github.com/bernardoleite/MAS-for-Answer-Extraction-and-QG/requirements.txt). If you are using a virtual environment for Python package management, you can install all python packages needed by using the following bash command:
    ```bash
    pip install -r requirements.txt
    ```
2. Install [nlpnet](https://github.com/erickrf/nlpnet) (as indicated by the author)
    ```python
    git clone https://github.com/erickrf/nlpnet
    cd nlpnet-master
    cython network.pyx
    python setup.py install
    ```
## Usage
1. Web Application
    ```bash
    cd web_app/
    python app.py
    ```
2. Command Line
    ```bash
    TODO
    ```
## Issues and Usage Q&A
To ask questions, report issues or request features, please use the GitHub Issue Tracker.

## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks in advance!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
### Project
This project is released under the **General Public License Version 3.0 (or later)**. For details, please see the file [LICENSE](https://github.com/bernardoleite/question-generation-portuguese/LICENSE) in the root directory.

### Third Party Components
Additionaly, this project includes third party software components: [stanfordnlp](https://github.com/stanfordnlp/stanfordnlp), [stanfordner](https://nlp.stanford.edu/software/CRF-NER.html), [nlpnet](https://github.com/erickrf/nlpnet), and this [ner portuguese model](https://rdm.inesctec.pt/pt_PT/dataset/cs-2017-005/resource/5456d599-8aed-49ed-b77c-6f66fe97cfbe) from this [masters thesis](https://github.com/arop/ner-re-pt). Each of these components have their own license. Please see [stanfordnlp/license](https://github.com/stanfordnlp/stanfordnlp/blob/master/LICENSE), [stanfordner](TODO), [nlpnet](https://github.com/erickrf/nlpnet/blob/master/LICENSE.txt), and the [ner portuguese model](https://rdm.inesctec.pt/pt_PT/dataset/cs-2017-005/resource/5456d599-8aed-49ed-b77c-6f66fe97cfbe) correspondingly.

### Commercial Purposes
A commercial license may also be available for use in industrial projects and collaborations that do not wish to use the GPL v3 (or later). Please contact the author if you are interested.

## References
If you use this software in your work, please kindly cite our research:
```bibtex
@mastersthesis{leite2020_ms,
    author = {Bernardo Leite},
    booktitle = {Dissertation for obtaining the Master Degree in Informatics and Computing Engineering},
    title = {Automatic Question Generation for the Portuguese Language},
    school = {Faculty of Engineering, University of Porto},
    url = {https://hdl.handle.net/10216/128541},
    day = {20},
    month = {07},
    year = {2020}
}

@inproceedings{leite2020_factoid,
    title={Factual Question Generation for the Portuguese Language},
    author={Leite, Bernardo and Cardoso, Henrique Lopes and Reis, Lu{\'\i}s Paulo and Soares, Carlos},
    booktitle={2020 International Conference on INnovations in Intelligent SysTems and Applications (INISTA)},
    pages={1--7},
    year={2020},
    organization={IEEE}
}
```

Also consider citing the third party software components. Please, see on their respective pages -- links above.

## Contacts
* Bernardo Leite, bernardo.leite@fe.up.pt
* Henrique Lopes Cardoso, hlc@fe.up.pt
* Luís Paulo Reis, lpreis@fe.up.pt