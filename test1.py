import spacy

text = """
The Government of India has accorded a major boost to the Indian Air Force’s (IAF) airborne surveillance and command capabilities with the approval of the AWACS India project, which envisages the procurement and development of six Airborne Early Warning and Control (AEW&C) aircraft based on the Airbus A321 platform.

The project, with an estimated cost of ₹19,000 crore (approximately $2.3 billion), will be spearheaded by the Defence Research and Development Organisation (DRDO) in partnership with Airbus and select Indian public and private sector firms.

This initiative underscores New Delhi’s larger vision of enhancing indigenous defence capabilities, reducing dependence on foreign imports for critical systems, and reinforcing self-reliance under the “Atmanirbhar Bharat” framework.

The choice of the Airbus A321 as the base aircraft marks a strategic shift from earlier projects involving smaller Embraer platforms. With significantly greater range, payload capacity, and endurance, the A321-based AEW&C aircraft will serve as a next-generation command and control hub.

These aircraft will integrate active electronically scanned array (AESA) radars, mission control systems, and indigenous electronic warfare suites designed by DRDO laboratories, providing the IAF with the ability to detect, track, and monitor multiple aerial and surface targets over extended ranges.

They will seamlessly function as force multipliers, not only enabling real-time situational awareness but also acting as airborne command posts to coordinate the employment of fighter jets, ground-based sensors, and air defence networks.

The approved program emphasises collaboration and indigenous content, with DRDO leading system design and mission integration, while Airbus provides the aircraft platform and technical support for modifications.
"""

nlp = spacy.load('en_core_web_sm')

doc = nlp(text)

for i in (doc.ents):
    print(f"{i.text} : {i.label_}")