# Text-Analysis-Project

Please read the [instructions](instructions.md).

**1. Project Overview** (~1 paragraph)

What data source(s) did you use? What technique(s) did you use to process or analyze them? What did yowu hope to create or learn through this project?

For this assignment I used Project Gutenberg to analyse the Novel Moby Dick in various ways. I did this in a few ways, one being a larger dictionary that would be used for investigation of the overall data. I also cleaned a string version of the text that was useful when looking at the novel chapter by chapter.  While I initially envisioned running some comparative analysis between novels, I found more value in continued analysis of Moby Dick and was able to continue finding new aspects to look into. I had hoped to learn more about working with dictionaries and loading large text/data into python as these were aspects of our course that really confused me in the past weeks. 

**2. Implementation** (~1-2 paragraphs)

Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice. Use shared links and/or screenshots to describe how you used GenAI tools to help you or learn new things.

Structuring my analysis file was acutally a much more involved process than I initially expected. Due to working with multiple functions and having to use a few different versions of the text depending on the desired output, it was critical that I ordered the functions correctly as to ensure that any neccesary analysis was done before further transformations could be done. My project began with loading the various libraries that would provide value during my investigation of the text. This is actually an area where generative AI was incredibly helpful as it would often reccomend me packages that could streamline existing code that I had written or allow for functionality that I didnt know was possible. One great example of this was the Counter function which comes from the Collections package. This made it much easier to count instances of words within each dictionary when looking at each chapter individually.

I then loaded in the novel using the Gutenberg Project. The first aspect of data processing was removing the project headers and ending, so the data found in analysis would be exclusively from the novel itself. I then stripped unnessecary characters from the text, and set all characters to lower to better account for comprehensive totals. My next function focused on cleaning the text in a string format so it could be used later for individual chapter analysis. This involved a similar process of the Gutenberg header skip and only selecting the string that existed between the starting case and ending case. I then used the cleaned text to seperate the novel into each chapter and created dictionaries based on each chapter and the most frequently occuring non stopwords in said chapter. After this initial data setup, I ran various functions that aimed to gather some information based on either the entire novel or each individual chapter. This was then consolidated in a main function at the end.

**3. Results** (~1-3 paragraphs + figures/examples)

Present what you accomplished in your project:

- If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
- If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.

This project was mainly focused on the analysis of Moby Dick. Being a very dense book, I was excited to see word distribution and how each chapter differed from one another. Moby Dick has 3 main types of storytelling, and each chapter generally falls into one of these categories: Technical Discussion of Sailing and Whaling, Plot driven or Narrative focused, and introspective/existential musings. After running my initial analysis of the Novel as a whole I wanted to dive into these topics and see if it was possible to classify each chapter to a given topic. 

My comprehensive analysis used many techniques we had learned in class. I was able to find total word count, the number of different words, the most common words, and the most common words without stopwords. These ended up being more or less what I was expecting, with the most common words being dominated by stopwords, and once removed we are let with words like "Whale", "Man", "Ahab", and "sea".
![alt text](<Screenshot 2024-11-02 161408.png>)

The chapter specific analysis was much more complex and I often had to utilize Generative AI to get feedback on broken code or help develop my train of though in order to keep functions manageable. It was also very helpful to ask the AI to give me a number of potential reasons why my code wasn't working when I ran into problems.
![alt text](<Screenshot 2024-11-01 143304.png>)

After breaking the text into each chapter using the delimiter of CHAPTER followed by 1-3 numbers, I made a dictionary with each chapter as the key and returned the 20 most common non stop words for each chapter. This returned similar results to the comprehensive analysis with Ahab and Whale topping most chapters, and words like boat and sea being frequent as well.
![alt text](<Screenshot 2024-11-02 162558.png>)

After seperating each chapter I was able to create a list of topics based on various words that were frequently seen in the Chapter dictionary. The goal for this was to count the instances of each kind of word and based on the totals, be able to guess what kind of chapter it was (technincal, introspective, narrative) However, this posed many issues as Moby Dick is a novel clouded by metaphor and complexity meaning it was very hard to find words that classified strongly into a certain category. For example, whale, while being a very common word really has no indicitive meaning as they are used throughout the book in the plot, during technical analysis, and are often metaphors during introspective moment. This meant that the most common word offered little to no value in this analysis. Given more time, or a reread of the book I believe this strategy could be improved upon greatly with different word selection.
![alt text](<Screenshot 2024-11-02 163300.png>)

**4. Reflection** (~1-2 paragraphs)

From a process point of view, what went well? What was the biggest challenge? How did you solve it? What could you improve? Was your project appropriately scoped? Did you have a good testing plan?

From a learning perspective, what was your biggest takeaway from this project? How did GenAI tools help you? How will you use what you learned going forward? What do you wish you knew beforehand that would have helped you succeed?

I think in this project I suceeded in creating interesting analysis of a complex novel I really enjoyed using skills that I was not particularly strong with. There was a large amount of coordination required for this project due to needing multiple versions of the data, and having to be comfortable with both strings and dictionaries. It was really challenging to keep all of it ordered correctly and using the adequate variables when using output from one function to the other. The main function was very helpful for this, but also required effort to stay on top of all the functions required to make things run as intended.

My biggest takeaway from this project is the importance of structure and intentional decesion making when beginning a project. As my ideas evolved with my analysis I had to shift functions around the file and change many variable names to avoid overlap. This made debugging much more complicated as the project went on because I always had multiple places to look when an error was made. Having a more concrete plan in the beginning would've saved me a lot of trouble as I couldve added my packages and built my functions from the ground up instead of frequently having to backtrack and re-adjust code as a result of wanting to add things in retroactively. Something I'd be excited to look into in the future is text clustering. I think there could have been a cool overlap between my "predicted" chapter classifcations and any word clusters I could have made from the chapters.


