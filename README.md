# pinecone_tutorial
Developing an embedding based question and answering service

To get running (a bit manual): 
1. Set up AWS. I use a t2.xlarge server. If you use tmux and git, you'll have to set it up. The default for Linux is python2.7 and you'll need it to install these packages. 
2. Coding for the project (python 3.7) will need to be in a venv. It's also helpful to tunnel to your browser if you use Jupyter (link here).Set up Feast and Pinecone. 
3. Feast has default data and files (example.py and test_example.py) that you'll want to delete and replace with the files from the GH repo. Pinecone requires you to signup and get an API key. 
4. Review the example.py and test_example.py files -- you'll need to modify some of the field names to complete the Pinecone tutorial, as the code is currently tweaked for the Google use case. Also, note that the timestamps are important when calling feast materialize. 
5. Follow the Pinecone tutorial, but execute my code in the notebooks. If you made the right changes to the files in Step #3, everything should work. :) 

Next steps: 
1. Scale from the 10K toy set to the 400K values.
2. Move this to an online service and redesign for incremental updates.
3. Set up a front end to receive queries and return Wikipedia titles with hyperlinks. 
