# Cockify
This is going to be a time tracking, ideally also a habi tracking, programm inspired by Clockify.

The lack of features and customizability bothered me and it's something I use daily, so it's a great choice for a personal project.

This sounds like an exciting project if I'm being honest, am happy to work on it.

## Technical aspects
Will use Github for version control. Later on I want to have a functioning website which I can use just like clockify, I in particular want to have a mySQL database connected to it and the ability to save my stuff onto it.

For the moment I think of having a project class which contains events with identifies, times and descriptions.

We could have a project "Programming" and an event-type "Cockify", then potential entries would be
of the form

Programming = {{"Cockify", sT, eT, "First Steps"}, {"Cockify", sT, eT, "Working on IO"}, {{"Checkers", sT, eT, "Adding the finishing touches"}}}

Then we have Programming.eventTypes = {"Cockify", "Checkers"}

We work with the assumption that there is only one time-thread running and therefore start and endtimes are unique. I want to index with starttimes as those are the interesting pieces of information.

One a good day I would reach not more than 20 individual entries in Clockify, so we can estimate a (very generous) upper bound on a years worth of entries to be 365 * 25 = 9125, if every entry is around 80 chars then that would need (without text optimizations which are very easily done) of 730000 bytes which is 0.73MB, so basically nothing.

So Website, Database and storing logic would be the main engineering parts of this project.

## Potential Branches
### Data Science
One nice thing about having a lot of exact data is that one can throw statistical magic onto it. So I'd like to either pipeline my data into data visualization stuff or even write my own from scratch. Although given that numpy is the prominent data science package I'm sure python has extremely strong data visualization capabilities.

Built in statistical Analysis would also be nice

### Habits and Gamification
If I'm tracking work times I might as well also track habits. And I liked the idea behind Habitica (also known as Habit RPG) of gamifying habit building. So I might use this stuff for my own purposes.

### Apppppppppppppppppppppppp
Could make a Phone App.

### Obsidian
Integrating this either by piping into Obsidian or even making an Obsidian Plugin would be a great way to connect the two tools I use most together.