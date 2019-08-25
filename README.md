# Testing Google Cloud Vision API On Handwritten Documents
A quick exploratory test using Google Cloud's Vision API to understand performance on three different types of handwritten documents:

Overall, the API does a pretty good job with handwritten text that are well formatted, clean and easy to read to the human eye. Even the ones that are smudgy, too cursive or usually difficult to read are returned with a decent accuracy although with a lower confidence and some errors in the predictions. There could be smarter ways to handle some of these errors (like looking for the closest meaningful English word etc. depending on the use case). Is there a specific type of handwriting that you might be interested in for the API?
 
### Tough Style:
 

 
Output – Confidence – 0.879
 
My mother , Jancy Delulty , always told her daughted as " Dand marry Chim until you see how the treats He waitress do How We treat there we ' re allowed to mistreat is the measure of who we are . Camie Schuell * handwritingday # moleskine .
 
 
### Tough Style 2:
 

 
Output: Confidence score – 0.8999
 
Start here . Politics is a contest os te napsative not a aselndent character , thus success in the political sphere is the product of best representing the relevant ideal not moral truth . this is is explored in b arn . which ende at didactically warns of candidates who e heign rather than embody & soultýs standards Last a repaesentation of immoratily catalyzed by | Elizabeth I ' s beinless signo | the relivision broadcast
 
### Medium Style:
 

 
Output: Confidence – 0.97
 
Reading a handwritten article about hand writing , in a 21st century magazine , is like listening to your great - great - grandfather shoot in the middle of a crowded multiplex about the incomparable glories of vaudeville and the lost art of wearing hats in public . And yet , somehow , here we are . Certain vestigial
 
### Easy Style:
 

 
Confidence – 0.92
 
It has shape - Shifted sevesal times , completely Throwing me off - track . efter a lot of observa tion , I have réalised that my dream has not morphed into something else . It is the same it was , but I have been defining it wrongly all these years . My dream is not to be a freelance Willustratoč as a freelance writes . My real dream is to live and work entirely on my Terms
 
### Easy Style 2:
 

 
Confidence – 0.977
 
Hello , everyone ! I made a Reddit account solely for the purpose of posting this . I often get compliments on my handwriting in school and I ' m curious to see what this thread thinks . I guess I ' ll write a few more lines so that you all have more content to evaluate . I ' m writing these words as they come to mind , so don ' t judge me for any grammatical errors . I hope this post doesn ' t get zero upvotes , that would be embarrassing . Thanks !

Performance evaluated based on output confidence scores and manual inspection and validation
