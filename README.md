*Summary*

Cosine similarity: MAX approach
Vectorization: Changed to seperate vectorization approach but used the vocabulary of vision in meta.

**Cosine Similarity** 

***Cosine Similarity Matrix Structure Detail:***

Rows: Vision statements.
Columns: Words in meta_words.
Objective:

For each vision statement (i.e., for each row), we want to find the maximum similarity value across all the words in meta_words (i.e., across all columns).
Axis Argument:

axis=0: Operates along the columns (i.e., finds the maximum similarity value for each word across all vision statements).
axis=1: Operates along the rows (i.e., finds the maximum similarity value for each vision statement across all words).
Since we want the maximum similarity value for each vision statement, we use axis=1. This way, we get a single maximum similarity value for each row (vision statement) by comparing it to all columns (words in meta_words).

***Example Illustration***
Assume similarity_matrix is as follows (with vision statements as rows and words in meta_words as columns):

    word1   word2   word3
vs1   0.2     0.8     0.1
vs2   0.5     0.3     0.7
vs3   0.6     0.4     0.2

For vision statement vs1 (first row), the similarities with word1, word2, and word3 are 0.2, 0.8, and 0.1 respectively. The maximum similarity is 0.8.
For vision statement vs2 (second row), the similarities are 0.5, 0.3, and 0.7. The maximum similarity is 0.7.
For vision statement vs3 (third row), the similarities are 0.6, 0.4, and 0.2. The maximum similarity is 0.6.
Using axis=1, we get the maximum similarity values for each vision statement:

similarity_percentages = similarity_matrix.max(axis=1) * 100

This results in:

similarity_percentages = [80.0, 70.0, 60.0]

Each value corresponds to the highest similarity percentage for each vision statement, representing how similar each vision statement is to any of the words in meta_words.

***MAX Approach***
As we have seen we are using max similarity.
See file src/vectorization line 40. (You can change this, read the alternatives below)
But when is max appropriate?

Identifying Strongest Match:
If you want to know the highest similarity score for each vision statement, which indicates the single word it matches best with in meta['UNK'].
This can be useful if the application requires identifying the closest match or the most relevant keyword for each vision statement.

When might max be less appropriate?

1. Overall Similarity Distribution:
If you are interested in the average similarity score or the overall distribution of similarities rather than just the maximum.
This might be the case if you want a more comprehensive view of how similar each vision statement is to the entire set of words in meta['UNK'].

2. Potential Outliers:
If there is a risk of outliers where a single high similarity score might be misleading.
For example, one vision statement might have a single high similarity score with one word but be dissimilar to all other words. This could be less informative than understanding the average similarity.

***Alternative Approaches***

1. Average Similarity:
You could calculate the average similarity score for each vision statement across all words in meta['UNK']:

similarity_averages = similarity_matrix.mean(axis=1) * 100

This provides a more balanced view of similarity.

2. Top-N Similarity:
Instead of the maximum, you could consider the top-N highest similarities and take an average:
python

top_n = 3  # Example for top-3 similarities
similarity_top_n = np.sort(similarity_matrix, axis=1)[:, -top_n:].mean(axis=1) * 100

This approach considers the top-N matches, providing a middle ground between max and mean.

3. Threshold-based Similarity:

Count how many similarities exceed a certain threshold:

threshold = 0.5  # Example threshold
similarity_above_threshold = (similarity_matrix > threshold).sum(axis=1)
This measures how many words in meta['UNK'] are significantly similar to each vision statement.

