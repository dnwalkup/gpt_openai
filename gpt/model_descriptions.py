# GPT4
gpt4_long = '''
GPT-4 is a large multimodal model (accepting text inputs and emitting text outputs today, with image inputs coming in the future) that can solve difficult problems with greater accuracy than any of our previous models, thanks to its broader general knowledge and advanced reasoning capabilities. Like gpt-3.5-turbo, GPT-4 is optimized for chat but works well for traditional completions tasks.
'''

gpt4_short = 'More capable than any GPT-3.5 model, able to do more complex tasks, and optimized for chat. Will be updated with our latest model iteration.'

gpt4_good = 'Good at: ... everything? '

gpt4_32k_long = '''
GPT-4 is a large multimodal model (accepting text inputs and emitting text outputs today, with image inputs coming in the future) that can solve difficult problems with greater accuracy than any of our previous models, thanks to its broader general knowledge and advanced reasoning capabilities. Like gpt-3.5-turbo, GPT-4 is optimized for chat but works well for traditional completions tasks.
'''
gpt4_32k_short = 'Same capabilities as the base gpt-4 mode but with 4x the context length. Will be updated with our latest model iteration.'

gpt4_32k_good = 'Good at: ... everything? '


# GPT3.5
gpt35_turbo_long = '''
Turbo is the same model family that powers ChatGPT. It is optimized for conversational chat input and output but does equally well on completions when compared with the Davinci model family. Any use case that can be done well in ChatGPT should perform well with the Turbo model family in the API.
\n
The Turbo model family is also the first to receive regular model updates like ChatGPT.
'''

gpt35_turbo_short = 'Most capable GPT-3.5 model and optimized for chat at 1/10th the cost of text-davinci-003. Will be updated with our latest model iteration.'

gpt35_turbo_good = 'Good at: Conversation and text generation'


# Davinci
davinci_long = '''
Davinci is the most capable model family and can perform any task the other models (ada, curie, and babbage) can perform and often with less instruction. For applications requiring a lot of understanding of the content, like summarization for a specific audience and creative content generation, Davinci will produce the best results. These increased capabilities require more compute resources, so Davinci costs more per API call and is not as fast as the other models.
\n
Another area where Davinci shines is in understanding the intent of text. Davinci is quite good at solving many kinds of logic problems and explaining the motives of characters. Davinci has been able to solve some of the most challenging AI problems involving cause and effect.
'''

davinci_short = 'Can do any language task with better quality, longer output, and consistent instruction-following than the curie, babbage, or ada models. Also supports inserting completions within text.'

davinci_good = 'Good at: Complex intent, cause and effect, summarization for audience'


# Curie
curie_long = '''
Curie is extremely powerful, yet very fast. While Davinci is stronger when it comes to analyzing complicated text, Curie is quite capable for many nuanced tasks like sentiment classification and summarization. Curie is also quite good at answering questions and performing Q&A and as a general service chatbot.
'''

curie_short = 'Very capable, faster and lower cost than Davinci.'

curie_good = 'Good at: Language translation, complex classification, text sentiment, summarization'


# Babbage
babbage_long = '''
Babbage can perform straightforward tasks like simple classification. It’s also quite capable when it comes to Semantic Search ranking how well documents match up with search queries.
'''

babbage_short = 'Capable of straightforward tasks, very fast, and lower cost.'

babbage_good = 'Good at: Moderate classification, semantic search classification'


# Ada
ada_long = '''
Ada is usually the fastest model and can perform tasks like parsing text, address correction and certain kinds of classification tasks that don’t require too much nuance. Ada’s performance can often be improved by providing more context.
'''

ada_short = 'Capable of very simple tasks, usually the fastest model in the GPT-3 series, and lowest cost.'

ada_good = 'Good at: Parsing text, simple classification, address correction, keywords'


# Whisper
whisper_long = '''
Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multi-task model that can perform multilingual speech recognition as well as speech translation and language identification. The Whisper v2-large model is currently available through our API with the whisper-1 model name.
\n
Currently, there is no difference between the open source version of Whisper and the version available through our API. However, through our API, we offer an optimized inference process which makes running Whisper through our API much faster than doing it through other means. For more technical details on Whisper, you can read the paper.
'''

# Codex
codex_long = '''
The Codex models are descendants of our GPT-3 models that can understand and generate code. Their training data contains both natural language and billions of lines of public code from GitHub. Learn more.
\n
They’re most capable in Python and proficient in over a dozen languages including JavaScript, Go, Perl, PHP, Ruby, Swift, TypeScript, SQL, and even Shell.
'''

codex_davinci_short = 'Most capable Codex model. Particularly good at translating natural language to code. In addition to completing code, also supports inserting completions within code.'

codex_cushman_short = 'Almost as capable as Davinci Codex, but slightly faster. This speed advantage may make it preferable for real-time applications.'

codex_good = 'Optimized for code-completion tasks'