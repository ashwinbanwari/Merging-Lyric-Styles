## Abstract
Throughout time and space, different artists have defined many different lyrical styles. From listening to a variety of songs, humans have a decent capacity to distinguish different artists, based just off lyrics. Can we train a model on our computers to do so, and even further, train a model to generate lyrics in that artists style? Text generation is a core problem in natural language processing. With the advent of massive language models like GPT-2, GPT-3, MT-NLG, we have become capable of producing significantly more realistic text than in the past.  Many of these models are transformer-based meaning that they can weight different parts of input data to get a better understanding of language and generate more logical text. We utilize these advances and focus on how well can we generate musical lyrics in the style of a particular artist using transfer learning from a pre-trained language model. 


## Problem Statement
We want to explore how well we can generate lyrics in a particular singer's style, and further, how well can we generate music in the combined style of two very different artists such that it has similarity to both of the singers independently. Specifically, we focus on the artists Beatles and Rihanna as they are two very different singers with lots of publically available lyrics. We use transfer learning from pre-trained GPT-2 to explore this and experiment with hyperparameters to generate reasonably musically sounding text that doesn't overfit and copy lines from input data. We finally explore ways to evaluate results and see how stylistically similar our generated lyrics for the Beatles is compared to real Beatles lyrics, how stylistically similar generated lyrics for Rihanna are compared to real Rihanna lyrics, and finally how stylistically similar our generated lyrics in their "mixed" style is to each of Beatles and Rihanna, independently. If we can generate text that is directly with style "in between" two different styles, it can have large implications on our understanding of language. 

<img src="https://www.rollingstone.com/wp-content/uploads/2010/12/BeatlesMainW.jpg" width="44%"/>        <img src ="https://media.istockphoto.com/vectors/black-plus-sign-positive-symbol-vector-id688550958?k=20&m=688550958&s=612x612&w=0&h=wvzUqT3u3feYygOXg3GB9pYBbqIsyu_xpvfTX-6HOd0=" width="9%"/>      <img src="https://thumbor.forbes.com/thumbor/1950x1950/filters%3Aformat%28jpg%29/https%3A%2F%2Fspecials-images.forbesimg.com%2Fimageserve%2F5ceec355142c500008f42068%2FRihanna-Diamond-Ball-Forbes-Women%2F0x0.jpg%3FcropX1%3D32%26cropX2%3D1982%26cropY1%3D257%26cropY2%3D2207" width="44%"/>

## Related Work
To extract the lyrics, we use Genius API stacked with lyricsgenius package made by John Miller (https://github.com/johnwmillr/LyricsGenius).
To evaluate the lyrics, we use modified minhash algorithm to fit into the Python 3 environment (https://github.com/rahularora/MinHash)
Much of this paper is only possible due to GPT-2, a language massive language model made by OpenAI. (https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
We were able to actually obtain the model parameters and perform additional training(transfer learning) thanks to the package gpt-2-simple package made by Max Woolfe (https://github.com/minimaxir/gpt-2-simple).

## Methodology

GPT-2 is one of the world's largest language models publicly available. It has 1.5 billion parameters and was trained on over 40GB of internet text over a long period of time. Training a comprehensive language model from scratch takes lots of time and input data, so we use this model to start with, then use transfer learning to try to generate lyrics in a particular artists style. Uniquely, we experiment with use mixed training set of two different artists to see how well we can generate lyrics that match the styles of different artists, and evaluate using BLEU on how well the generated lyrics match either of the individuals styles.

In this project, we use a pre-trained language model(GPT-2) and use transfer learning to let our model learn and embed a type of English in the style of a particular artist. Specifically, we make three models, in the style of Beatles, in the style of Rihanna, and in the mixed style of the two (using both their lyrics as input to the model). Then, we generate lyrics using each of the models. Finally, we evaluate our result. We mix songs from The Beatles and Rihanna in the training data, to see if we can make our model generate "mixed" style lyrics that feature aspects of both artist. Lyrics are extracted using the lyricsgenius package. Then, using transfer learning from GPT2, we let our model generate lyrics, and we evaluate the generated output using the minhash algorithm to compare its similarity to "true" lyrics of artists it was trained on.

First, we use gpt-2-simple to obtain the model parameters and then utilize its API to set hyperparameters like iterations and learning rate. What we do is then use transfer learning. Specifically, using the pretrained model, we do FURTHER training on particular training data. Specifically, we use three sets of training data, Beatles lyrics dataset, Rihanna lyrics dataset, and a mixed dataset with both of their lyrics. We use lyricsgenius package to generate these datasets. For each of these datasets, we find optimal hyperparameters and train it for 400-600 iterations depending on the size of the dataset (and to avoid overfitting as noticed happening when training for too long). Once we make models that are sufficiently trained on the particular datasets with low loss, we generate text using the GPT-2 model. It is a transformer-based models similar to those in past homework (except with two decoders instead of one), and we use it to generate next character giving some past charactars, thus generating text of arbitrary length. Once we generate text for our three models, we use the minhash algorithm which was our best method to measure stylistic similarity. To measure stylistic similarity was a very difficult ask, as most text similarity methods are based on _semantic_ meaning, rather than style, however this was the best approach we found. 

To use the lyricgenius package, we put artists' names inside a list and specify the number of songs we need for each artist.
To use the minhash algorithm, we put generated songs in files and run "python minhash.py" to determine similarity.
## Experiments

## Results

## Figures

 Figure 1: Loss w/ Beatles Training Data
 
 ![](beatles.png)
 
 Figure 2: Loss w/ Rihanna Training Data
 
 ![](GPT-2%20Loss%20with%20Rihanna%20Training%20Data.png)
 
 
 Figure 3: Loss w/ Mixed Training Data
 
 ![](GPT-2%20Loss%20with%20Beatles%2BRihanna%20Training%20Data.png)

 
 Figure 4 generated text after 200 iteration of training on Beatles
 
```
======== SAMPLE 1 ========
 better at the wheel), but I do love when I can drive the car on the corner

  No, I won't burn

  Don't make it worse, don't make it worse 

(Oh yeah, see you next time)<|endoftext|>New York City has been rocked by a mass shooting since the start of the new year. So what is an "angel of death"?

The New York Times

There is no word yet on the cause of death of the first person to be killed in the shooting in a Jewish market in Paris on Feb. 13, 2012. (Eve Shopham/The Washington Post)

The first-person shooter

No, not a Jewish man
Who told you to "shoot the Jews"?

When we pray together,
We've got your back

We just need to be mindful of each other

You're breathing life into this world,
Shall we go check on him?
(He's dead)

The mother fucker
Why don't you tell him to stop?
(You're dead)

It's impossible for him to see through these eyes
Because he's too young to be here
He needs your love

Love in the form of his life
You're crying wolf
You know what I like about him?
A loving brother and a kind heart
Love in all its forms<|endoftext|>Tottenham Hotspur 0-2 Manchester City
It was a close call at the Etihad Stadium when Spurs took pride in the result as they fell within six points of Premier League leaders Manchester City.
The visitors took the lead shortly before half-time when Danny Rose headed in a fine save from the top scorer just seconds after the break and it was not long before City began to slip back into the draw.
Kanu played a key part in the first half through Andre Villas-Boas in place of Wijnaldum and though Spurs were still in the game, they were too far to play from behind.
The hosts made it four with an equaliser but City were fortunate to be in the game in the box. A fine move by Pochettino put the home side up three as Spurs found the break three minutes from time in injury time after half-time before City responded with another on goal.
At half-time, City found the back of the net in what was undoubtedly an impressive effort from Ritchie and they had just enough to make it three before the break.
Kanu had a fine offload in the 64th minute as Dele Alli opened the scoring in the first 20 minutes and it was City who found the net just minutes on as Tiote headed in a low low shot from distance. Tiote had the chance just moments before too late in the break as the Argentine was headed in by a free kick from a shot near the top corner but he was too late as Wayne Rooney raced down to finish the ball off Kane.
Cameron Viggo behind the scenes had the game against them as he had the lone shot from cover but he could not make it past Jozy Altidore in the 86th minute. City had the shots though as the visitors were level on the break when Van Persie brought the ball into position and had them up high before the break when the Spaniard was brought down by a shot from distance.
O'Meara had the game flowing with crosses from Alvaro Morata and the hosts had the ball in their hands as the Brazilian was given the chance to finish off Kane in the 89th minute but he was not there to make it past Mata in the 88th minute as O'Meara went over for Kane before the break.
With City 1-1 at home to the winners of a Premier League away league and the away side in last place, City had the run of form they needed and just six minutes into the second half it looked like the hosts might be just their half as they went into the break in the game they lost in Burnley to win it all in a game they had won just over a month earlier.
The hosts found the back of the net just two minutes from time in the 86th minute when Tiote ran wide from the penalty spot, he looked unstoppable as he was cleared off the ball by Joe Allen and he was saved early on while City went down 2-1 in the 16th minute when Kane had the chance to make it five in a row when the Argentine was saved by the space and the space of space behind him.
City had the ball in their hands moments later with Van Persie unmarked as they had a challenge on Michael Carrick and the home crowd were just eight points clear at the top of the Premier League so they had the momentum to take to the game they had lost in Burnley.
With eight minutes to play in the first half, City had their shots in their hands as Tiote had the chance to make it eight in a
```

 ## Demo

## Video

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/ashwinbanwari/Merging-Lyric-Styles/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
