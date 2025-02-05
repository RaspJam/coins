<img width=280 alt="Drawing of a coin split in half, where three cog wheels emerge" src="media/coins.png" align="left"></img>


<br />
<div align="center">
  <div id="user-content-toc">
    <ul>
      <summary><h1 style="display: inline-block;">TL;DR</h1></summary>
    </ul>
    COINS is an acronym coined by <a href="https://github.com/btatkerson">btatkerson</a> to simplify how voice commands are understood. This repository shares the idea of a coin and stores the code for training the COINS NER model.
  </div>
</div>
<br /><br /><br /><br />

<!--# to be filled in...-->
# Training
> [!WARNING]
> Python 3.9 is the verified working version; any version, newer or older, may not function properly.

The COINS model is trained using [spaCy](https://spacy.io/); as such, this section is akin to their [docs#usage](https://spacy.io/usage). If you have trouble with spaCy, please review their docs before creating an [issue here](https://github.com/RaspJam/coins/issues)! To train the model, simply:

1. Install required dependencies
```sh
python3 -m pip install -r requirements.txt
```

2. Create a file for annotated data (more info at [acoin](https://github.com/RaspJam/acoin))
```sh
echo "Please [set](COMMAND) a [timer](OPTION) for [15](NUMBER) [minutes](INPUT)" > annotations.txt
```

3. Run the training script
```sh
python3 main.py
```

This will export the model in the root directory under the name `COINS`, this can then be passed to Ellie for use. You may also want to test the model, which can be done by running
```sh
python3 src/test.py
```
