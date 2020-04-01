# Tagup DevOps Coding challenge

Thanks for your interest in joining our team! This challenge is a simple test for us to evaluate your technical abilities.

## Challenge Description

The challenge is to develop a simple AWS S3 storage analysis tool.
The tool must be executable from the command line, and must return a list of all [S3](https://aws.amazon.com/documentation/s3/) buckets accessible to the user. For each bucket, the tool should display the following information: 
- Bucket name
- Creation date
- Number of files
- Total size of files (an option should permit to display it in bytes, kB, MB, ...)
- Last modified date of the most recent file

The tool must work on Linux and OSX, and the installation process must be clearly documented. Ideally, your tool won't require installation of any other tools / libraries / frameworks to work.

Your are free to use the programming language and the [SDK](https://aws.amazon.com/tools/) of your choice. You may assume the user has `bash`, `python3`, and `pip` installed on their system; any other executables and libraries must be included as part of the installation process. The installation process should be quick and easy, and the documentation must cover installation on both Ubuntu 18.04 and OSX.

Your project should be hosted on github and be a standalone project (i.e. **do not fork it from our challenge or any other project**).

## Tips

Try to design and implement your solution as you would do for real production code. Show us how you create clean and maintainable code that produces awesome result. Build something that we'd be happy to contribute to.

Feel free to add more features: we're curious about what you can think of. We'd expect the same if you worked with us!

Documentation and tests are always a huge plus.
