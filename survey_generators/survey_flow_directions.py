pg1 = """
We are working on a non-profit project for research purposes to identify <b>company acquisitions</b> and <b>mergers</b> from a large number of business headlines.
<br><br>
An <b>acquisition</b> is when one company buys another company. 
<br><br>
A <b>merger</b> is when two companies join together as equals.
"""

pg2 = """
<b>Your role is to read each headline presented and answer three questions:</b>
<br><br>
1. Does the headline describe a company acquisition? <br>
2. Does the headline describe a company merger? <br>
3. What is the <b>name of the company</b> that is the acquirer (the buyer)? <br>
4. What is the <b>name of the company</b> that is acquired (bought)?
"""

pg3 = """
Sometimes, you will <b>not be sure</b> about the answers. 
<br><br>
<ul>
<li>If you are not sure if the headline is an acquisition, you can enter "unclear."</li>
<li>If the headline does not say, or you are not sure who is the acquirer or acquired company, leave one or both text boxes blank.</li>
<li>For mergers, the companies join as equals. Order does not matter. Enter the <b>name of each company</b> in the text boxes.</li>
</ul>
"""

pg4 = """
Your task is to review a maximum of XXX headlines, which will take about XX hours.
<br><br>
First, we will provide training. We will show you examples of headlines and how they should be classified.
<br><br>
Second, we will give you a test. We will show you headlines we have already tested and record your answers. <b>If you classify most of the test headlines correctly, you will move on to the next task.</b> If there are too many errors, we will pay you for your time but you will not be able to proceed with more work.
<br><br>
Third, you will start the work of reading headlines and recording acquisitions. <b>NOTE: we will periodically include test headlines at random intervals to check that you are paying attention.</b> If you do not answer these questions correctly, we will end your session. We will pay you for your time but you will not be able to proceed with the work.
"""

pg5 = """
<b>{}</b>
<br><br>
This headline is about an <b>acquisition</b>. We click "Acquisition" in the drop-down box.
<br><br>
In this headline, {} acquires {}. 
<br><br>
We COPY and PASTE the names of the company that was the acquirer (the buyer) and the aquiree (the company purchased).
"""

pg6 = """
<b>{}</b>
<br><br>
This headline is about an acquisition. We click "Acquisition" in the drop-down box.
<br><br>
This headline uses the passive voice: {} was <b>acquired by</b> {}. For this headline, COMPANY2 is the acquirer and COMPANY1 the acquiree.
<br><br>
We COPY and PASTE the correct names into the text boxes.
"""

pg7 = """
<b>{}</b>
<br><br>
This headline is about a <b>merger</b>. We click "Merger" in the drop-down box.
<br><br>
The headline says which companies are in the mergers. For mergers, the order does not matter. 
<br><br>
We COPY and PASTE the names into the text boxes, in either order.
"""

pg8 = """
<b>{}</b>
<br><br>
This headline is not about an acquisition or merger. We click "Not merger or acquisition" in the drop-down box
"""

pg9 = """
<b>{}</b>
<br><br>
This headline is about an <b>acquisition</b>. It talks about a company being "bought," which is another way of saying acquired. We click "Acquisition" in the drop-down box.
<br><br>
This headline writes that {} was the acquirer. But it does not say who the acquired company was. 
<br><br>
We COPY and PASTE {} in the acquirer box, and leave the "acquiree" box blank, and move to the next, clicking the forward arrow.
"""

pg10 = """
<b>{}</b>
<br><br>
This headline is about an <b>acquisition</b>. It talks about a company being "purchased," which is another way of saying acquired. We click "Acquisition" in the drop-down box.
<br><br>
This headline writes that {} was acquired. But it does not say what company was the acquirer.
<br><br>
We COPY and PASTE COMPANY2 in the acquiree box, and leave the "acquirer" box blank, and move to the next, clicking the forward arrow.
"""

pg11 = """
Test headline 6. 
<br><br>
It is unclear if this headline is about an acquisition. So we click "Unclear" in the drop-down box.
"""

pg12 = """
Training is complete! Remember, your task is to:
<br><br>
<ol>
<li>Decide if you think the headline refers to an acquisition or merger. Some other words used are purchased or bought.</li>
<li>If you think the headline is about an acquisition or merger, enter that in the drop-down box.</li>
<li>If the headline is not about an acquisition or merger, click “Not about an acquisition or merger” in the drop-down box.</li>
<li>If you are not sure, click “Unclear.” It is better to be conservative. If you are at all unsure, click “unclear.” Don’t spend too long deciding.</li>
<li>For headlines that are an acquisition or merger, the next step is to fill out the text boxes. COPY and PASTE the name of the acquirer company and the acquired company.</li>
<li>If you are not sure the names of the companies, leave one or both text boxes blank.</li>
</ol>
"""

pg13 = """
Some tips before you start:
<br><br>
<ol>
<li>It is faster to use your keyboard (not your mouse) to move to different fields. If you TAB, you will move to the next field. You can select the drop-down box response with the first letter: “A”, “M”, “N” or “U”</li>
<li>To enter the names of the companies, you will need to use your mouse to highlight the name to COPY and PASTE.</li>
</ol>
"""

pg14 = """
REMEMBER: it is most important to be accurate. DO NOT RUSH. 
<br><br>
<b><i>We will be including “test” headlines in random places to check your work.</i></b>
<br><br>
Once the task is complete, we will assign you a code for you to enter. IT IS IMPORTANT YOU ENTER THE CORRECT CODE. We will use this code to issue payment for the work you have done.
<br><br>
Let’s get started!
"""
