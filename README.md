# Reddit Line Breaks Fixer

This is a simple program that automatically converts single line-break text from your clipboard like this:

    Roses are red
    Violets are blue

**Output:**

*Roses are red
    Violets are blue*

into double line-break text like this:

    Roses are red

    Violets are blue

**Output 1:**

*Roses are red*

*Violets are blue*

so that it can be used on pages like Reddit, StackOverflow, Github... where a double line break is needed to make a new paragraph.

The alternate method consists on adding two spaces at the end of the lines instead of a double line-break to make the distance smaller:

    Roses are red  // <---Double space here
    Violets are blue

**Output 2:**

*Roses are red*  
*Violets are blue*

It is so simple it is self-explanatory but it's basically a regular expression that replaces `\n` with the correct expression depending on the selected mode: `  \n` and `\n\n` respectively. But it comes in pretty handy and I use it myself so I thought I'd upload it here.

## Example:

![Pic1](https://i.imgur.com/yXkiZrG.png)
