### Problem

I'm a massive football fan and I was on a mission to snag tickets for the FIFA Women's World Cup match between Australia and France. I literally spent hours browsing the official website and checking out resale platforms, all in the hopes of getting those golden tickets. But here's the kicker – every time adult tickets popped up, I was way too slow to grab 'em.

I mean, seriously, the whole process was like a broken record: log in, pick the match, refresh the page a million times for tickets. It was driving me nuts! So, being the tech-savvy person I am, I put on my thinking cap and decided to tackle the problem head-on. I cooked up this idea to create an automated system that would magically toss adult tickets into my cart.

No more endless website loops, no more frantic logins. And guess what? It actually worked! I not only got myself a ticket but hooked up a bunch of my buddies too. Cheers to tech wizardry and never missing out on the football action again! 🎉

### Prerequisites

- Chrome browser installed on your system
- Python 3.9 and above
- PowerShell
- Slack webhook URL (For notifications)

### How to run

##### Method 1: Easiest way to run the app is through PowerShell

1. Download this repository on your computer
2. Simply open a PowerShell terminal
3. Change directory (cd) to the location of the downloaded repository
4. Run `./run-local.ps1`. This will ask you to fill in your fifa username and password, the url to the ticket page, and slack web hook url for notifications. 
5. Keep an eye out for a slack notification or your cart
6. If you need to edit your credentials or other config you can open the `.env` file within the repository

##### Method 2: Old school

1. Download this repository on your computer

2. Add a `.env` file with the following information 
   ```
   USERNAME=<fifa username here>
   PASSWORD=<fifa password here>
   TARGET_URL=<fifa match ticket url>
   HOOK_URL=<slack webhook url>
   ```

3. In a new terminal, change directory to the repository folder and run `main.py`

4. Keep an eye out for a slack notification or your cart

### Gotchas (IMPORTANT! MUST READ)

1. This script can yield false positives. While tickets might appear as "available" on the website, but they could actually be in the checkout process.
2. Captchas and waiting rooms can disrupt the automation process for acquiring game tickets. These disruptions compelled me to perform certain steps manually, ensuring the smooth operation of my automation. This included occasionally signing out of my account, waiting for 5 minutes before rerunning the script, or extending the sleep timers to 60 seconds (line 30) in `main.py`. I had to run the script, complete captchas, and wait in the rooms to allow the script to proceed.
3. The page refreshes every second (the optimal rate). Reducing this frequency could potentially overload FIFA's website or result in your IP being blocked.
4. Once the script manages to add a ticket to your cart. Make sure to process the payment within 9 minutes. This and the rest of the steps are manual. 

It would have been great to execute this script headlessly on a cloud server to automatically secure my tickets. However, as I mentioned earlier, this approach would be challenging due to the need for certain manual steps.

### Signs you have a ticket in your cart

- Your terminal will show "=================  HIT! ================="
- You receive a slack notification (If you have provided a webhook url)
- The page redirects you to your cart or payment page

### Potential Improvements

- Enhance the PowerShell script to validate user inputs thoroughly.
- Implement comprehensive unit testing.
- Provide users with the choice to utilise either Chrome or Edge browsers.
- Implement an automated mechanism for populating credit card information.
- Enable the purchase of a specified quantity, n, of tickets.

### Demo

![Demo](https://github.com/jsantias/fifa-wwc-2023-ticket-fetcher/images/demo.gif)

### Did this work?

Be sure to Star this repository and share it with your mates!

### Support

[Buy me a coffee!]: https://bmc.link/jbsantias

# Go the Matildas!!!!

My view at the Australia vs France game

![IMG_9014](https://github.com/jsantias/fifa-wwc-2023-ticket-fetcher/images/IMG_9014.jpg)