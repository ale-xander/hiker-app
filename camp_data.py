# camp_data.py

CAMP_KNOWLEDGE = {
    "Sanborn": {
        
  "1": {
    "vibe": "Group-Friendly Standard Hike-In (lower loop)",
    "privacy": 2,
    "shade": "Full",
    "pros": "In the lower loop closest to parking; part of the 1–3 cluster that works very well for multi-family groups; very short uphill walk.",
    "cons": "Sites here are fairly close together with significant group noise and foot traffic; little sense of seclusion.",
    "best_for": "Two or three families booking adjacent sites and wanting the easiest possible haul from car to camp.",
    "tags": ["standard-hike-in", "lower-loop", "group-friendly", "easy-access", "low-privacy"]
  },
  "2": {
    "vibe": "Group-Friendly Standard Hike-In (lower loop)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Part of the 1–3 cluster praised for multi-family camping; very short, gentle hike-in under tall redwoods.",
    "cons": "Minimal separation from neighboring sites; better for groups that know each other than for solo campers.",
    "best_for": "Families or friends booking more than one adjacent site in the 1–3 group.",
    "tags": ["standard-hike-in", "lower-loop", "group-friendly", "easy-access", "low-privacy"]
  },
  "3": {
    "vibe": "Group-Friendly Standard Hike-In (lower loop)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Completes the 1–3 group cluster; convenient for shared meals and kid play between sites; easy walk from parking.",
    "cons": "Little visual or sound separation between camps; not well-suited to people seeking quiet.",
    "best_for": "Multi-family trips and social camping more than private retreats.",
    "tags": ["standard-hike-in", "lower-loop", "group-friendly", "easy-access", "low-privacy"]
  },
  "4": {
    "vibe": "Group-Friendly Standard Hike-In (lower loop)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Part of the 4–6 cluster recommended for camping with several families; still in the easier lower section of the hill.",
    "cons": "Close-packed pads mean noise and activity from neighbors are constant when multiple sites are filled.",
    "best_for": "Coordinated groups booking 4–6 as a shared camp area.",
    "tags": ["standard-hike-in", "lower-loop", "group-friendly", "easy-access", "low-privacy"]
  },
  "5": {
    "vibe": "Group-Friendly Standard Hike-In (lower loop)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Central site among 4–6, convenient as a hub for group gear and meals; short walk from the cart area.",
    "cons": "Even less privacy than edge sites; surrounded on both sides when 4 and 6 are occupied.",
    "best_for": "Families or friends who plan to use all three of 4–6 together.",
    "tags": ["standard-hike-in", "lower-loop", "group-friendly", "easy-access", "low-privacy"]
  },
  "6": {
    "vibe": "Group-Friendly Standard Hike-In (lower loop)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Third member of the 4–6 cluster; enjoys the same easy access and thick shade as the rest of the lower loop.",
    "cons": "Little sense of separation from neighboring sites, especially when booked by unrelated parties.",
    "best_for": "Multi-family groups; not ideal for solo campers wanting quiet.",
    "tags": ["standard-hike-in", "lower-loop", "group-friendly", "easy-access", "low-privacy"]
  },
  "7": {
    "vibe": "Standard Hike-In (lower loop)",
    "privacy": 3,
    "shade": "Full",
    "pros": "Lower loop site within the recommended 1–10 band; easier hike-in with full redwood shade and creek ambience.",
    "cons": "Sanborn’s walk-in sites are fairly close together, so neighboring camps will still feel near.",
    "best_for": "Families and casual campers who want convenience but don’t need maximum privacy.",
    "tags": ["standard-hike-in", "lower-loop", "easy-access", "family-friendly", "cluster-level-only"]
  },
  "8": {
    "vibe": "Standard Hike-In (lower loop, group-capable)",
    "privacy": 3,
    "shade": "Full",
    "pros": "Included in the suggested 1–8 plus 10 mega-cluster; still relatively close to parking with strong shade.",
    "cons": "When many adjacent sites are booked, it feels busy and social rather than secluded.",
    "best_for": "Larger gatherings booking multiple lower-loop sites, or families wanting easy access.",
    "tags": ["standard-hike-in", "lower-loop", "group-friendly", "easy-access", "cluster-level-only"]
  },
  "9": {
    "vibe": "Semi-Secluded \"Best Single\" Hike-In",
    "privacy": 4,
    "shade": "Full",
    "pros": "Widely recommended as the best single-family site; relatively large with good privacy, its own path to a nearby toilet and creek, and not directly next to other sites; has nicer views than many pads.",
    "cons": "Tent pad area has a noticeable slope, so you must hunt for the flattest tent spots.",
    "best_for": "Single families or small groups wanting the best mix of privacy, beauty, and reasonable hike-in effort.",
    "tags": ["premium", "semi-secluded", "lower-loop", "near-bathroom", "near-creek", "best-all-around"]
  },
  "10": {
    "vibe": "Edge-of-Loop Standard Hike-In",
    "privacy": 3,
    "shade": "Full",
    "pros": "Functionally part of the lower cluster despite numbering; very close to site 1 and the 1–8 grouping, with easy access from parking.",
    "cons": "Limited privacy due to its proximity to heavily used lower-loop sites.",
    "best_for": "Families who want easy access and are comfortable near large, social groups.",
    "tags": ["standard-hike-in", "lower-loop", "easy-access", "cluster-level-only"]
  },
  "11": {
    "vibe": "Standard Hike-In (mid band)",
    "privacy": 3,
    "shade": "Full",
    "pros": "In the 11–13 zone that remains manageable for average fitness; a middle-distance option between the bottom and top.",
    "cons": "No specific distinguishing details; likely shares the overall snug spacing of Sanborn’s walk-in campground.",
    "best_for": "Campers who want to be a bit removed from the lowest sites without committing to a long climb.",
    "tags": ["standard-hike-in", "mid-band", "moderate-hike", "cluster-level-only", "low-confidence"]
  },
  "12": {
    "vibe": "Convenient, Family-Friendly Standard Hike-In",
    "privacy": 3,
    "shade": "Full",
    "pros": "Mid-campground area near the band of restrooms and creek access; moderate hike-in distance but strong amenity access.",
    "cons": "Higher foot traffic around restroom paths and water access; not ideal if you dislike people passing by.",
    "best_for": "Families with kids and campers who prioritize proximity to bathrooms and water.",
    "tags": ["standard-hike-in", "mid-band", "near-bathroom", "near-creek", "family-friendly", "cluster-level-only", "moderate-confidence"]
  },
  "13": {
    "vibe": "Standard Hike-In (mid band)",
    "privacy": 3,
    "shade": "Full",
    "pros": "Upper end of the 11–13 stretch, still within reasonable reach for average fitness.",
    "cons": "No site-specific reports; privacy and layout inferred from general campground descriptions.",
    "best_for": "Campers seeking a mid-hill compromise rather than extreme convenience or extreme distance.",
    "tags": ["standard-hike-in", "mid-band", "moderate-hike", "cluster-level-only", "low-confidence"]
  },
  "14": {
    "vibe": "Standard Hike-In (start of upper hill)",
    "privacy": 3,
    "shade": "Full",
    "pros": "Transition into the steeper upper hillside, likely with fewer casual walkers from the parking lot.",
    "cons": "Noticeably steeper gear haul than lower-loop sites; specific privacy features are unknown.",
    "best_for": "Fit couples or small groups wanting to edge into the quieter upper section.",
    "tags": ["standard-hike-in", "upper-hill", "steep-hike", "cluster-level-only", "low-confidence"]
  },
  "15": {
    "vibe": "Standard Hike-In (upper hill)",
    "privacy": 3,
    "shade": "Full",
    "pros": "Part of the higher-number band roughly 1/4–1/2 mile from the car, so fewer casual visitors wander past.",
    "cons": "Steeper, longer approach and more effort for bathroom and water runs; privacy not clearly better than other sites.",
    "best_for": "Fit campers who want to be above the heavily used lower section.",
    "tags": ["standard-hike-in", "upper-hill", "steep-hike", "cluster-level-only", "low-confidence"]
  },
  "16": {
    "vibe": "Standard Hike-In (upper hill)",
    "privacy": 3,
    "shade": "Full",
    "pros": "Upper-section shade and canyon ambience with more distance from RV traffic.",
    "cons": "Strenuous hike with gear and longer walks back to the car; spacing is inferred rather than documented.",
    "best_for": "Adults comfortable with a more strenuous hike-in who mainly care about being away from the entrance.",
    "tags": ["standard-hike-in", "upper-hill", "steep-hike", "cluster-level-only", "low-confidence"]
  },
  "17": {
    "vibe": "Group-Friendly Standard Hike-In (upper mid cluster)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Part of the specifically recommended 17–19 trio for groups that know each other; good for shared activities.",
    "cons": "Very limited privacy when not part of a group booking; high mutual visibility among the three sites.",
    "best_for": "Groups reserving 17–19 together; not solo campers.",
    "tags": ["standard-hike-in", "upper-mid", "group-friendly", "steep-hike"]
  },
  "18": {
    "vibe": "Group-Friendly Standard Hike-In (upper mid cluster)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Central site in the 17–19 cluster; natural group common space when all three are booked.",
    "cons": "Maximum noise and activity when neighbors are present; little physical separation.",
    "best_for": "Friend groups or multi-family trips using 17–19 as a shared area.",
    "tags": ["standard-hike-in", "upper-mid", "group-friendly", "steep-hike"]
  },
  "19": {
    "vibe": "Group-Friendly Standard Hike-In (upper mid cluster)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Completes the 17–19 trio; good for multi-tent groups who want to stay close together.",
    "cons": "Little seclusion when used on its own; part of a tight group cluster.",
    "best_for": "Groups that intentionally book all of 17–19.",
    "tags": ["standard-hike-in", "upper-mid", "group-friendly", "steep-hike"]
  },
  "20": {
    "vibe": "Upper-Band Standard Hike-In",
    "privacy": 3,
    "shade": "Full",
    "pros": "In the higher-number band that is significantly uphill, giving more distance from RV and day-use noise.",
    "cons": "Longer and steeper gear haul; site-specific spacing and views are undocumented.",
    "best_for": "Fit campers who want to be up the hill and away from the entrance bustle.",
    "tags": ["standard-hike-in", "upper-band", "steep-hike", "cluster-level-only", "low-confidence"]
  },
  "21": {
    "vibe": "Upper-Band Standard Hike-In",
    "privacy": 3,
    "shade": "Full",
    "pros": "Heavily shaded and quiet in terms of vehicle noise due to distance.",
    "cons": "Strenuous logistics for water and car access; privacy estimate is based only on overall campground design.",
    "best_for": "Adults camping light who value being removed from the lower clusters.",
    "tags": ["standard-hike-in", "upper-band", "steep-hike", "cluster-level-only", "low-confidence"]
  },
  "22": {
    "vibe": "Upper-Band Standard Hike-In",
    "privacy": 3,
    "shade": "Full",
    "pros": "Deep forest shade and creek sounds below, far from car noise.",
    "cons": "Long return to facilities; no direct reports on how close it is to neighbors.",
    "best_for": "Experienced campers who prefer quiet and don’t mind a long walk.",
    "tags": ["standard-hike-in", "upper-band", "steep-hike", "cluster-level-only", "low-confidence"]
  },
  "23": {
    "vibe": "Upper-Band Standard Hike-In",
    "privacy": 3,
    "shade": "Full",
    "pros": "Shares the remote, forested feel of the upper walk-in canyon away from day-use activity.",
    "cons": "Steep, extended hike with gear; privacy attributes are inferred from general campground patterns only.",
    "best_for": "Fit adults or couples wanting an upper-loop experience.",
    "tags": ["standard-hike-in", "upper-band", "steep-hike", "cluster-level-only", "low-confidence"]
  },
  "24": {
    "vibe": "Upper-Band Standard Hike-In",
    "privacy": 3,
    "shade": "Full",
    "pros": "One of the more distant sites, maximizing the feeling of being removed from the RV area.",
    "cons": "Cumbersome logistics for bathroom and car trips; no clear evidence it is more private than other upper sites.",
    "best_for": "Campers planning to stay put and minimize trips back to the car.",
    "tags": ["standard-hike-in", "upper-band", "steep-hike", "cluster-level-only", "low-confidence"]
  },
  "25": {
    "vibe": "Upper-Band Standard Hike-In",
    "privacy": 3,
    "shade": "Full",
    "pros": "Very shaded and away from vehicle noise; good for people who dislike generators and traffic.",
    "cons": "Physically demanding to bring in car-camping loads; spacing unknown beyond general snug campground design.",
    "best_for": "Experienced, fit campers with minimalist setups.",
    "tags": ["standard-hike-in", "upper-band", "steep-hike", "cluster-level-only", "low-confidence"]
  },
  "26": {
    "vibe": "Upper-Band Standard Hike-In",
    "privacy": 3,
    "shade": "Full",
    "pros": "Among the higher-numbered sites, delivering strong forest immersion and distance from the road.",
    "cons": "One of the longest and steepest approaches; not recommended for new campers with heavy gear.",
    "best_for": "Seasoned campers and backpacker-style trips treating the hike as part of the experience.",
    "tags": ["standard-hike-in", "upper-band", "steep-hike", "cluster-level-only", "low-confidence"]
  },
  "27": {
    "vibe": "Upper-Band Standard Hike-In",
    "privacy": 3,
    "shade": "Full",
    "pros": "Very quiet in terms of vehicle noise, with dense redwood shade.",
    "cons": "Extra-cumbersome logistics due to slope and distance; no evidence of exceptional privacy compared with neighbors.",
    "best_for": "Adults who want very quiet nights and are okay with long walks to amenities.",
    "tags": ["standard-hike-in", "upper-band", "steep-hike", "cluster-level-only", "low-confidence"]
  },
  "28": {
    "vibe": "Upper-Band Standard Hike-In",
    "privacy": 3,
    "shade": "Full",
    "pros": "Located in the upper walk-in corridor where Sanborn’s generally low crowding is most noticeable.",
    "cons": "Steep, lengthy hike-in that may feel punishing with kids or bulky equipment; privacy details are unknown.",
    "best_for": "Couples and small groups that camp light and prefer fewer nearby cars.",
    "tags": ["standard-hike-in", "upper-band", "steep-hike", "cluster-level-only", "low-confidence"]
  },
  "29": {
    "vibe": "Upper-Band Standard Hike-In",
    "privacy": 3,
    "shade": "Full",
    "pros": "Heavily shaded and away from RV generators and vehicles.",
    "cons": "Among the farthest walks to parking and showers; neighboring spacing is not documented.",
    "best_for": "Experienced campers who value distance from vehicles more than campsite-to-campsite separation.",
    "tags": ["standard-hike-in", "upper-band", "steep-hike", "cluster-level-only", "low-confidence"]
  },
  "30": {
    "vibe": "Semi-Secluded Upper Single Hike-In",
    "privacy": 4,
    "shade": "Full",
    "pros": "Specifically recommended as a great site for a single family, located higher up the hill for added distance from busy lower clusters.",
    "cons": "Much steeper, longer walk from the car than lower-loop sites; more work for every trip back to the parking area.",
    "best_for": "Fit families or couples who want a more private feel and don’t mind a serious uphill.",
    "tags": ["premium", "semi-secluded", "upper-band", "steep-hike", "best-for-privacy"]
  },
  "31": {
    "vibe": "Upper-Band Standard Hike-In (very high)",
    "privacy": 3,
    "shade": "Full",
    "pros": "One of the highest-numbered sites, with maximum distance from the entrance and RV area.",
    "cons": "Very long, steep haul with gear; site-specific privacy characteristics are unknown.",
    "best_for": "Strong hikers and minimalist campers who want to be far from the parking lot.",
    "tags": ["standard-hike-in", "upper-band", "steep-hike", "cluster-level-only", "low-confidence"]
  },
  "32": {
    "vibe": "Upper-Band Standard Hike-In (very high)",
    "privacy": 3,
    "shade": "Full",
    "pros": "Near the top of the walk-in network, maximizing the feeling of being away from the lower campground.",
    "cons": "One of the longest and steepest approaches; no public descriptions of unique privacy or view advantages.",
    "best_for": "Experienced, fit campers seeking a near-backcountry feel in a managed park.",
    "tags": ["standard-hike-in", "upper-band", "steep-hike", "cluster-level-only", "low-confidence"]
  },
  "33": {
    "vibe": "Upper-Band Standard Hike-In (furthest)",
    "privacy": 3,
    "shade": "Full",
    "pros": "Highest-numbered tent site in the 33-site walk-in corridor, giving the maximum distance from the parking lot and RV campground.",
    "cons": "Likely the steepest and longest hike with gear, and furthest from amenities; privacy score kept conservative due to lack of site-specific reports.",
    "best_for": "Very fit, experienced campers who want to be as far up the hill as possible.",
    "tags": ["standard-hike-in", "upper-band", "steep-hike", "most-remote", "cluster-level-only", "low-confidence"]
  }

    
    },

    "Mt Madonna Park": {
  "118N": {
    "vibe": "Valley View 1 tent site in mixed RV/tent loop",
    "privacy": 2,
    "shade": "Partial",
    "pros": "Easy drive-in access in Valley View 1 with sun and shade mix; very kid-friendly loop with good bike/scooter riding and quick walks to flush bathrooms and free hot showers.",
    "cons": "Valley View 1 has nearby RV sites with partial hookups, so tent sites like this one may be adjacent to RVs and occasional generator noise; inner-loop feel with neighbors close on multiple sides.",
    "best_for": "Families who prioritize easy access, full facilities, and kid bike loops over privacy and generator-free quiet.",
    "tags": ["standard-car-camping", "tent-only", "loop-valley-view-1", "partial-shade", "family-friendly", "kid-bike-loop", "near-rv-hookups", "possible-generator-noise", "cluster-level-only"]
  },
  "119N": {
    "vibe": "Valley View 1 tent site in mixed RV/tent loop",
    "privacy": 2,
    "shade": "Partial",
    "pros": "Drive-in tent site with convenient access to Valley View 1 amenities, including clean restrooms, free showers, and kid-friendly paved loop.",
    "cons": "Located in the same loop as RV hookup sites, so RVs and generators may be close by; typical inner-loop spacing with limited privacy.",
    "best_for": "Families and new campers who want maximum convenience and amenities and can tolerate RV neighbors.",
    "tags": ["standard-car-camping", "tent-only", "loop-valley-view-1", "partial-shade", "family-friendly", "kid-bike-loop", "near-rv-hookups", "possible-generator-noise", "cluster-level-only"]
  },
  "120N": {
    "vibe": "Valley View 1 tent site in mixed RV/tent loop",
    "privacy": 2,
    "shade": "Partial",
    "pros": "Short walk to bathrooms, showers, and trailheads; good combination of redwood and open sky typical of Valley View 1.",
    "cons": "Shares the loop with RV hookup pads, increasing the chance of generator hum and vehicle activity near your tent; sites are fairly close together.",
    "best_for": "Car-camping families who want showers, bikes, and kid infrastructure more than a secluded forest feel.",
    "tags": ["standard-car-camping", "tent-only", "loop-valley-view-1", "partial-shade", "family-friendly", "kid-bike-loop", "near-rv-hookups", "possible-generator-noise", "cluster-level-only"]
  },
  "121N": {
    "vibe": "Valley View 1 tent site in mixed RV/tent loop",
    "privacy": 2,
    "shade": "Partial",
    "pros": "Convenient car-side camping with easy navigation for kids and quick access to showers and potable water.",
    "cons": "Loop includes RV and hookup sites, so nearby generators and parked rigs can undercut the tent-camping vibe; not ideal for light sleepers.",
    "best_for": "Families comfortable in a classic county-park loop with mixed rigs and lots of kid activity.",
    "tags": ["standard-car-camping", "tent-only", "loop-valley-view-1", "partial-shade", "family-friendly", "kid-bike-loop", "near-rv-hookups", "possible-generator-noise", "cluster-level-only"]
  },
  "122N": {
    "vibe": "Valley View 1 tent site in mixed RV/tent loop",
    "privacy": 2,
    "shade": "Partial",
    "pros": "Part of the main Valley View 1 complex with close access to well-maintained bathrooms, free showers, amphitheater, and kid programs.",
    "cons": "High likelihood of being near RVs due to partial-hookup sites in the same loop; sites are not widely spaced, so noise and headlights are more noticeable.",
    "best_for": "Campers seeking full amenities and kid activities who can ignore occasional generator and vehicle noise.",
    "tags": ["standard-car-camping", "tent-only", "loop-valley-view-1", "partial-shade", "family-friendly", "kid-bike-loop", "near-rv-hookups", "possible-generator-noise", "cluster-level-only"]
  },
  "123N": {
    "vibe": "Valley View 1 tent site in mixed RV/tent loop",
    "privacy": 2,
    "shade": "Partial",
    "pros": "Tent-designated pad with car-side convenience and access to Valley View 1’s clean bathrooms, showers, and kid-friendly loop road.",
    "cons": "In a loop that supports RVs with hookups, so neighboring sites may be trailers or motorhomes with generators; inner-loop density keeps privacy low.",
    "best_for": "Families who want a very easy, infrastructure-rich campground and aren’t sensitive to RV presence.",
    "tags": ["standard-car-camping", "tent-only", "loop-valley-view-1", "partial-shade", "family-friendly", "kid-bike-loop", "near-rv-hookups", "possible-generator-noise", "cluster-level-only"]
  },

  "201": {
    "vibe": "Valley View 2 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Drive-in site in Valley View 2 with mix of sun and redwood shade; generally quieter and more tent-oriented than Valley View 1 while still close to bathrooms and water.",
    "cons": "Still a car-camping loop with neighbors nearby and some small RVs or trailers possible; not a true forest hideaway.",
    "best_for": "Families and couples who want a balance of convenience and a bit more calm than the main RV-heavy loop.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-2", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "202": {
    "vibe": "Valley View 2 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Typical Valley View 2 pad with easy car-side setup, a blend of sun and trees, and short walks to clean restrooms and showers.",
    "cons": "Loop layout means sites are still relatively close together; occasional generator noise from small RVs is possible, though less common than in Valley View 1.",
    "best_for": "Car campers fine with a bit of activity who want a slightly mellower loop.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-2", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "203": {
    "vibe": "Valley View 2 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Comfortable compromise loop with forest setting, good facilities, and less RV focus than Valley View 1.",
    "cons": "Privacy is moderate rather than high; camps are within easy sight and sound of one another.",
    "best_for": "Families and small groups wanting full amenities in a less intense loop.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-2", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },

  "204": {
    "vibe": "Valley View 2 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Drive-in pad typical of Valley View 2, with drinking water and flush toilets a short walk away and kid-friendly roads for scootering.",
    "cons": "Still close to neighbors and loop traffic; some chance of nearby small RVs or trailers.",
    "best_for": "Car-camping families comfortable with a moderate level of campground noise.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-2", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "205": {
    "vibe": "Valley View 2 family-friendly tent site near bathrooms",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Frequently recommended as a great choice for families because it is close to the bathrooms and showers while still in a quieter, more tent-focused loop than Valley View 1.",
    "cons": "Proximity to facilities means more foot traffic and kid activity along the path; still a car-camping loop, not secluded.",
    "best_for": "Families with younger kids who need quick bathroom access and like being near the action without the RV concentration of Valley View 1.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-2", "partial-shade", "family-friendly", "near-bathroom", "moderate-privacy"]
  },

  "206": {
    "vibe": "Valley View 2 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Sun/shade mix with nearby family amenities; good middle-of-the-road site for most tent campers.",
    "cons": "Average privacy; you will still see and hear adjacent sites clearly.",
    "best_for": "General-purpose car camping with full services close by.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-2", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "207": {
    "vibe": "Valley View 2 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Same advantages as other VV2 sites: forest ambience, partial shade, and nearby showers without as many hookups as VV1.",
    "cons": "Moderate noise and traffic along the loop road; not a high-privacy location.",
    "best_for": "Campers who want a versatile, kid-friendly campsite and aren’t chasing absolute quiet.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-2", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },

  "208": {
    "vibe": "Valley View 2 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Solid all-around site for tents in a mixed-sun redwood environment with flush toilets and showers nearby.",
    "cons": "Clustered loop layout; you’ll be aware of neighboring camps’ noise and lights.",
    "best_for": "Typical family car-camping trips with kids and simple gear.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-2", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "209": {
    "vibe": "Valley View 2 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Close to trail access and central loop amenities; easy to manage for new campers and kids.",
    "cons": "Moderate noise from nearby sites; not a retreat-style campsite.",
    "best_for": "First-time or occasional campers who want something easy and predictable.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-2", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },

  "210": {
    "vibe": "Valley View 2 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Forest feel with quick access to showers and toilets; a good default choice if you just want a normal site.",
    "cons": "Limited separation between pads along the loop; average privacy only.",
    "best_for": "Campers who mostly value comfort and ease of use over a special or standout setting.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-2", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "211": {
    "vibe": "Valley View 2 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Good access to both campground amenities and trails; typical Valley View 2 experience.",
    "cons": "You will hear and see your neighbors; occasional small RVs may share the loop.",
    "best_for": "Flexible car campers without strong privacy demands.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-2", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "212": {
    "vibe": "Valley View 2 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Sun and shade mix with standard Mt. Madonna amenities: food locker, table, fire ring, and nearby water.",
    "cons": "Moderately busy loop with average distance between campsites.",
    "best_for": "Typical family camping weekends.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-2", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },

  "213": {
    "vibe": "Valley View 2 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Balanced exposure and shade; easy access to restrooms and trailheads.",
    "cons": "Standard loop density; not particularly high or low privacy.",
    "best_for": "Campers who just want a normal, functioning site with no special requirements.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-2", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "214": {
    "vibe": "Valley View 2 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Typical Valley View 2 feel with decent space and facilities nearby.",
    "cons": "Ambient noise and lights from neighboring sites remain part of the experience.",
    "best_for": "Relaxed car-camping without specific site preferences.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-2", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "215": {
    "vibe": "Valley View 2 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Comfortable car-side camping with common amenities a short walk away.",
    "cons": "Average privacy; camp feels like a normal county-park loop rather than a hideout.",
    "best_for": "Groups and families comfortable with hearing and seeing neighbors.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-2", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "216": {
    "vibe": "Valley View 2 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Good mix of redwood atmosphere and services, with convenient car access.",
    "cons": "Campground layout keeps all sites within relatively close proximity.",
    "best_for": "Classic drive-in camping with kids and friends.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-2", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "217": {
    "vibe": "Valley View 2 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Standard VV2 pad with decent room for a tent and picnic area.",
    "cons": "Limited distance to neighboring pads; normal campground noise levels.",
    "best_for": "General-purpose family camping.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-2", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "218": {
    "vibe": "Valley View 2 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Comfortable, service-rich campsite typical of Mt. Madonna.",
    "cons": "Not notably more private or more open than other VV2 sites.",
    "best_for": "Campers without particular site demands beyond having a spot.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-2", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "219": {
    "vibe": "Valley View 2 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Same access and amenities as the rest of Valley View 2; fine for most uses.",
    "cons": "Average privacy and average noise; nothing particularly standout.",
    "best_for": "Backup or overflow choice when other favorites are booked.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-2", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "220": {
    "vibe": "Valley View 2 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Typical car-camping pad with good park infrastructure and mixed forest setting.",
    "cons": "Limited separation from neighboring sites; not a special high-privacy pick.",
    "best_for": "Campers who are happy with any functional VV2 site.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-2", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "221": {
    "vibe": "Valley View 2 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "End of the Valley View 2 numbering, still offering easy access to facilities and trails.",
    "cons": "Privacy remains moderate; nearby camps are still within clear view and earshot.",
    "best_for": "Non-picky campers who value reliability and amenities.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-2", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },

  "301": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Drive-in site in a more tent-focused Valley View loop with sun and shade mix; close to bathrooms and water with a family-friendly layout.",
    "cons": "Sites remain relatively close together; occasional small RVs or trailers may share the loop.",
    "best_for": "Families and couples who want a straightforward, amenity-rich redwood campground experience.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },

  "302": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Typical VV3 pad with a balance of forest shade and openings; easy access to clean restrooms and showers.",
    "cons": "Shares the usual loop density, so privacy is moderate at best.",
    "best_for": "General-purpose family car camping.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "303": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Comfortable drive-in campsite with ready access to trails and kids’ activities.",
    "cons": "Neighboring sites are close; not a quiet backcountry-style site.",
    "best_for": "Families with kids who will use bikes, scooters, and the nearby trails.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },

  "304": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Easy car-side setup, standard amenities, and a mix of redwood and oak woodland around camp.",
    "cons": "Campground feel is social rather than secluded; you’ll hear nearby loops and traffic.",
    "best_for": "Relaxed weekend car camping.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "305": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Same full-service experience as the rest of Valley View 3; works for most tent setups.",
    "cons": "Not notably more private or special than its neighbors.",
    "best_for": "Campers who are satisfied with any available VV3 site.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },

  "306": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Easy access to both park activities and basic services; good standard car-camping feel.",
    "cons": "Neighbors are close enough that noise and lights will be present.",
    "best_for": "Families and small groups who care more about amenities than uniqueness.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },

  "307": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Balanced exposure and shade; straightforward campsite with typical SCCP infrastructure.",
    "cons": "Standard loop density yields average privacy only.",
    "best_for": "General car camping with kids or friends.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },

  "308": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Close enough to bathrooms and showers to be convenient, far enough that they’re not in your lap.",
    "cons": "All the sites in this loop share a similar level of neighbor proximity.",
    "best_for": "Non-picky campers seeking a reliable redwood campsite with services.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },

  "309": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Typical VV3 pad, appropriate for tents and small rigs with normal gear.",
    "cons": "Ambient loop noise; no special privacy or separation.",
    "best_for": "Standard weekend outings.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },

  "310": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Forest feel and kids’ friendly loop with minimal navigation complexity.",
    "cons": "Average privacy; typical campground noise levels.",
    "best_for": "Families and friends who will spend as much time exploring as at camp.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "311": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Straightforward pad suitable for one or two tents and standard camp setup.",
    "cons": "Sharing the loop’s standard close spacing and social vibe.",
    "best_for": "Most car-camping use cases without special constraints.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },

  "312": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Access to Mt. Madonna’s trails, amphitheater, and family activities from a normal, service-rich loop.",
    "cons": "Not suitable for travelers seeking substantial isolation.",
    "best_for": "Families planning to take advantage of on-site kid activities and nearby attractions like Gizdich Ranch and Gilroy Gardens.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },

  "313": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Flexible, no-fuss pad for tents or small rigs in a good overall location.",
    "cons": "Loop design limits the feeling of personal space.",
    "best_for": "Easygoing campers who care more about location than micro-details.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },

  "314": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Same pros as other VV3 sites—convenient and kid-friendly.",
    "cons": "Standard campground proximity; no special privacy or view advantage documented.",
    "best_for": "Typical tent-camping weekends.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "315": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Good base for exploring both the park’s trails and nearby day trips.",
    "cons": "Campground-style bustle rather than solitude.",
    "best_for": "Groups who will be out and about a lot.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "316": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Works for a wide range of basic tent setups, including small families.",
    "cons": "No evidence of special layout or separation benefits versus neighbors.",
    "best_for": "Backup or overflow selection in VV3.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "317": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Usual Mt. Madonna pros: clean restrooms, free showers, forest setting.",
    "cons": "Average noise and proximity to neighbors; not a standout site.",
    "best_for": "Campers without strong site preferences.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "318": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Good general-use campsite with moderate privacy within a family-friendly loop.",
    "cons": "Loop layout inherently limits seclusion.",
    "best_for": "Most family and friend group trips.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "319": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Balanced site in a popular, feature-rich park.",
    "cons": "No specific per-site perks beyond the loop norms.",
    "best_for": "Flexible campers focused on the park as a whole.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "320": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Representative of VV3’s mix of forest and facilities; fine for most uses.",
    "cons": "Close neighbors and loop traffic keep it from feeling remote.",
    "best_for": "Campers used to standard state/county-park style camping.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "321": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Same access to nearby trails and facilities as other VV3 camps; suitable for tents and small rigs.",
    "cons": "Typical campground visibility and noise from nearby sites.",
    "best_for": "Families looking for reliability over uniqueness.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "322": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Good all-around site when availability is limited; easy car access.",
    "cons": "Nothing particularly special about privacy or layout based on published information.",
    "best_for": "Overflow or practical choice when first-pick sites are taken.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "323": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Adequate space for a typical family tent, picnic area, and fire ring under mixed canopy.",
    "cons": "Neighborhood of similar sites means few unique advantages beyond location.",
    "best_for": "Non-specialized camping trips.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "324": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "Appropriate for common family car-camping setups.",
    "cons": "No additional separation or view perks identified in text sources.",
    "best_for": "Default VV3 choice.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },
  "325": {
    "vibe": "Valley View 3 standard tent/drive-in site",
    "privacy": 3,
    "shade": "Partial",
    "pros": "End-of-range VV3 site still benefiting from all loop amenities and forest environment.",
    "cons": "Standard loop proximity and noise.",
    "best_for": "Campers who mainly need a functioning campsite with services.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-valley-view-3", "partial-shade", "family-friendly", "moderate-privacy", "cluster-level-only"]
  },

  "401": {
    "vibe": "Tan Oak loop tent/drive-in site (quieter forest feel)",
    "privacy": 4,
    "shade": "Full",
    "pros": "Drive-in site in Tan Oak loop, generally quieter and more tent-oriented than Valley View loops; deeper redwood shade and more of a forest-retreat feeling while still having flush toilets and potable water nearby.",
    "cons": "Less sun and more dampness than the mixed-sun Valley View loops; still a loop campground, so some neighbor noise is inevitable.",
    "best_for": "Tent campers and families who prefer a quieter, more wooded atmosphere with fewer RVs and a more retreat-like feel.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-tan-oak", "full-shade", "more-private", "quieter-loop", "family-friendly", "cluster-level-only"]
  },
  "402": {
    "vibe": "Tan Oak loop tent/drive-in site (quieter forest feel)",
    "privacy": 4,
    "shade": "Full",
    "pros": "Heavily shaded redwood site in a generally calmer loop; good for hammock time and forest immersion.",
    "cons": "Cooler and damper microclimate may be a downside for some; privacy is better than Valley View but not absolute.",
    "best_for": "Campers wanting a more subdued, woodsy loop within Mt. Madonna.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-tan-oak", "full-shade", "more-private", "quieter-loop", "family-friendly", "cluster-level-only"]
  },
  "403": {
    "vibe": "Tan Oak loop tent/drive-in site (quieter forest feel)",
    "privacy": 4,
    "shade": "Full",
    "pros": "Classic redwood-feel campsite with more distance from RV hookups and main activity loops.",
    "cons": "Less direct sun for drying gear; further drive or walk to the amphitheater and Valley View activities.",
    "best_for": "Couples or small families wanting a calmer nighttime soundscape.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-tan-oak", "full-shade", "more-private", "quieter-loop", "cluster-level-only"]
  },

  "404": {
    "vibe": "Tan Oak loop tent/drive-in site (quieter forest feel)",
    "privacy": 4,
    "shade": "Full",
    "pros": "Sheltered among tall trees with less through-traffic than Valley View; feels more tucked away.",
    "cons": "Can feel dark and chilly, especially in shoulder seasons; easier to get damp gear.",
    "best_for": "Campers who prioritize quiet and forest ambience over warmth and sun.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-tan-oak", "full-shade", "more-private", "quieter-loop", "cluster-level-only"]
  },
  "405": {
    "vibe": "Tan Oak loop tent/drive-in site (quieter forest feel)",
    "privacy": 4,
    "shade": "Full",
    "pros": "Good option for those avoiding RV-heavy loops; shaded and relatively peaceful within the campground context.",
    "cons": "Smaller windows of direct sunlight; may feel a bit gloomy to some campers.",
    "best_for": "Forest lovers who like long, cool evenings by the fire.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-tan-oak", "full-shade", "more-private", "quieter-loop", "cluster-level-only"]
  },

  "406": {
    "vibe": "Tan Oak loop tent/drive-in site (quieter forest feel)",
    "privacy": 4,
    "shade": "Full",
    "pros": "Quieter loop away from hookups and yurts, giving more chance at restful nights.",
    "cons": "Further from some kid-focused amenities compared with Valley View 1.",
    "best_for": "Families comfortable walking or driving a bit farther to activities in exchange for calmer camping.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-tan-oak", "full-shade", "more-private", "quieter-loop", "family-friendly", "cluster-level-only"]
  },
  "407": {
    "vibe": "Tan Oak loop tent/drive-in site (quieter forest feel)",
    "privacy": 4,
    "shade": "Full",
    "pros": "Immersive redwood setting with fewer RVs and less motor noise.",
    "cons": "Cool and damp conditions; extra layers and drying strategies recommended.",
    "best_for": "Experienced tent campers and hammock enthusiasts.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-tan-oak", "full-shade", "more-private", "quieter-loop", "cluster-level-only"]
  },
  "408": {
    "vibe": "Tan Oak loop tent/drive-in site (quieter forest feel)",
    "privacy": 4,
    "shade": "Full",
    "pros": "Strong sense of being in the woods, yet within a short drive or walk of all park amenities.",
    "cons": "Not ideal for those who like sunny camps or warm mornings.",
    "best_for": "Campers seeking a forest cocoon within a county park.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-tan-oak", "full-shade", "more-private", "quieter-loop", "cluster-level-only"]
  },

  "409": {
    "vibe": "Tan Oak loop tent/drive-in site (quieter forest feel)",
    "privacy": 4,
    "shade": "Full",
    "pros": "Generally quieter than Valley View loops with more distance from RV hookups and amphitheater.",
    "cons": "Less central to kid programming and presentation areas if that’s a priority.",
    "best_for": "Families who value peace and forest surroundings more than constant activity.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-tan-oak", "full-shade", "more-private", "quieter-loop", "family-friendly", "cluster-level-only"]
  },
  "410": {
    "vibe": "Tan Oak loop tent/drive-in site (quieter forest feel)",
    "privacy": 4,
    "shade": "Full",
    "pros": "Consistently shaded, cooler in hot weather and farther from the RV-heavy Valley View 1 loop.",
    "cons": "Darker atmosphere, potentially muddy or damp after storms.",
    "best_for": "Heat-averse campers and those chasing quiet redwood vibes.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-tan-oak", "full-shade", "more-private", "quieter-loop", "cluster-level-only"]
  },

  "411": {
    "vibe": "Tan Oak loop tent/drive-in site (quieter forest feel)",
    "privacy": 4,
    "shade": "Full",
    "pros": "Loop design and tree cover create a more sheltered, less trafficked atmosphere.",
    "cons": "Less adjacency to activity hubs; may feel too still for some kids.",
    "best_for": "Adults or older kids who like peaceful forest settings.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-tan-oak", "full-shade", "more-private", "quieter-loop", "cluster-level-only"]
  },
  "412": {
    "vibe": "Tan Oak loop tent/drive-in site (quieter forest feel)",
    "privacy": 4,
    "shade": "Full",
    "pros": "More secluded feel than Valley View, with fewer RV spots and less vehicle movement.",
    "cons": "Same potential dampness and cool microclimate that characterize Tan Oak.",
    "best_for": "Campers who don’t mind cooler temps in exchange for quiet.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-tan-oak", "full-shade", "more-private", "quieter-loop", "cluster-level-only"]
  },
  "413": {
    "vibe": "Tan Oak loop tent/drive-in site (quieter forest feel)",
    "privacy": 4,
    "shade": "Full",
    "pros": "Heavily forested site in a loop often noted as calmer than Valley View.",
    "cons": "Less ideal for sun-lovers and those wanting frequent trips to amphitheater events.",
    "best_for": "People who read, relax, and hang in hammocks at camp.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-tan-oak", "full-shade", "more-private", "quieter-loop", "cluster-level-only"]
  },
  "414": {
    "vibe": "Tan Oak loop tent/drive-in site (quieter forest feel)",
    "privacy": 4,
    "shade": "Full",
    "pros": "Deep forest ambience plus all the basic amenities of Mt. Madonna.",
    "cons": "Same condensation and dampness trade-offs as other Tan Oak sites.",
    "best_for": "Forest-focused camping trips with minimal focus on structured kid events.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-tan-oak", "full-shade", "more-private", "quieter-loop", "cluster-level-only"]
  },
  "415": {
    "vibe": "Tan Oak loop tent/drive-in site (quieter forest feel)",
    "privacy": 4,
    "shade": "Full",
    "pros": "Well-suited for those who want to fall asleep to forest sounds rather than RV or amphitheater noise.",
    "cons": "Longer walks or drives back to central attractions and loops.",
    "best_for": "Campers who like to stay put at camp and enjoy the woods.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-tan-oak", "full-shade", "more-private", "quieter-loop", "cluster-level-only"]
  },
  "416": {
    "vibe": "Tan Oak loop tent/drive-in site (quieter forest feel)",
    "privacy": 4,
    "shade": "Full",
    "pros": "Part of the quieter Tan Oak loop, generally away from RV hookups and heavy traffic.",
    "cons": "Cool and sometimes damp; can feel remote relative to other loops if kids want constant structured activities.",
    "best_for": "Adults or families who self-entertain at camp.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-tan-oak", "full-shade", "more-private", "quieter-loop", "cluster-level-only"]
  },
  "417": {
    "vibe": "Tan Oak loop tent/drive-in site (quieter forest feel)",
    "privacy": 4,
    "shade": "Full",
    "pros": "Nice option for tent campers seeking a more back-to-nature vibe within a managed campground.",
    "cons": "Less sun for solar gear or morning warmth.",
    "best_for": "Forest and cool-weather fans.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-tan-oak", "full-shade", "more-private", "quieter-loop", "cluster-level-only"]
  },
  "418": {
    "vibe": "Tan Oak loop tent/drive-in site (quieter forest feel)",
    "privacy": 4,
    "shade": "Full",
    "pros": "Edge-of-park ambience with strong redwood presence and fewer RV neighbors.",
    "cons": "Still not completely isolated; other Tan Oak camps are visible and audible.",
    "best_for": "Campers who prefer the quieter loop but understand it’s still a developed campground.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-tan-oak", "full-shade", "more-private", "quieter-loop", "cluster-level-only"]
  },
  "419": {
    "vibe": "Tan Oak loop tent/drive-in site (quieter forest feel)",
    "privacy": 4,
    "shade": "Full",
    "pros": "Shares Tan Oak’s more tranquil character and strong forest feel.",
    "cons": "Cooler temps and dampness may bother some campers.",
    "best_for": "Those who enjoy cozy, woodsy camping and don’t mind bundling up.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-tan-oak", "full-shade", "more-private", "quieter-loop", "cluster-level-only"]
  },
  "420": {
    "vibe": "Tan Oak loop tent/drive-in site (quieter forest feel)",
    "privacy": 4,
    "shade": "Full",
    "pros": "Good choice for avoiding RV-dense areas and kid-heavy bike loops.",
    "cons": "Further from some of the more structured kid offerings and amphitheater events.",
    "best_for": "Campers who prefer quiet evenings over busy loops.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-tan-oak", "full-shade", "more-private", "quieter-loop", "cluster-level-only"]
  },
  "421": {
    "vibe": "Tan Oak loop tent/drive-in site (quieter forest feel)",
    "privacy": 4,
    "shade": "Full",
    "pros": "Edge-of-loop site within the quietest of Mt. Madonna’s main campgrounds; strong redwood atmosphere.",
    "cons": "Same cool, damp conditions as other Tan Oak sites; still moderate neighbor noise.",
    "best_for": "Campers who want Mt. Madonna’s forest setting with the best odds of a calmer night.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "loop-tan-oak", "full-shade", "more-private", "quieter-loop", "cluster-level-only"]
  }
},
    "Uvas Canyon Park": {
  "1": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (entrance-side)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Very short drive and walk from the campground entrance; full canyon shade with nearby creek sounds; quick access to bathrooms and trailheads in this compact campground.",
    "cons": "Sites at Uvas Canyon are lined closely along the narrow road and creek, so privacy is limited and you will clearly hear neighbors; more vehicle movement near the entrance.",
    "best_for": "Families or small groups arriving late or wanting the shortest possible setup time while still enjoying waterfalls and shade.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "full-shade", "very-close-sites", "near-entrance", "waterfall-hikes", "cluster-level-only"]
  },
  "2": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (entrance-side)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Near the front of the campground with quick access to restrooms and water; strong tree cover and consistent creek ambience.",
    "cons": "Little visual or sound separation from neighboring pads; expect a social, family-heavy feel rather than solitude.",
    "best_for": "Campers prioritizing convenience, shade, and easy navigation over privacy.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "full-shade", "very-close-sites", "near-entrance", "waterfall-hikes", "cluster-level-only"]
  },
  "3": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (entrance-side)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Short walk from parking pad to table and fire ring; good staging point for short waterfall hikes; same lush, shaded feel as the rest of the loop.",
    "cons": "Tight spacing along the campground road; conversations and kids’ voices from neighboring sites carry easily.",
    "best_for": "Families who want easy logistics and don’t mind being close to other campers.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "full-shade", "very-close-sites", "near-entrance", "waterfall-hikes", "cluster-level-only"]
  },
  "4": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (central creekside)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Representative central-site experience with full shade, creek noise, and short walks to both bathrooms and trailheads; suitable for tents and small rigs.",
    "cons": "Like most Uvas sites, pads are close together and parallel to the road and creek, so you will hear neighboring groups and possibly occasional small RV generators.",
    "best_for": "Campers who care more about easy access to waterfalls and shade than about spacing between sites.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "creekside", "full-shade", "very-close-sites", "family-weekend-spot", "cluster-level-only"]
  },
  "5": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (central)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Short, flat walk from car to tent area with nearby water spigot and restrooms; easy for first-time or kid-heavy trips.",
    "cons": "Minimal privacy; expect neighboring tents and vehicles to be very close by on both sides.",
    "best_for": "Beginners and families who want low-effort camping in a very small, amenity-rich county park.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "full-shade", "very-close-sites", "family-weekend-spot", "cluster-level-only"]
  },
  "6": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (central, flatter pad)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Typical shaded, creek-adjacent site with a relatively flat parking pad that works well for tents, rooftop tents, and small RVs; near the heart of the loop and facilities.",
    "cons": "Close proximity to neighboring sites and road traffic; likely to experience both family noise and occasional small RV generator use nearby.",
    "best_for": "Families or small groups who value a flat pad and convenience over privacy.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "full-shade", "rooftop-tent-friendly", "very-close-sites", "family-weekend-spot", "cluster-level-only"]
  },
  "7": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (central, flatter pad)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Full shade, clean nearby restrooms, and a relatively level parking/tent area compared with some neighboring pads; easy camp setup.",
    "cons": "Part of the closely spaced central row of sites; expect a social canyon-camp feel, not seclusion.",
    "best_for": "Tent or rooftop-tent campers who want easy setup and don’t mind close neighbors.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "full-shade", "rooftop-tent-friendly", "very-close-sites", "family-weekend-spot", "cluster-level-only"]
  },
  "8": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (central row)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Short walk to the main restroom building and trailheads; same lush, shaded canyon feel as the rest of the campground.",
    "cons": "Tight spacing and aligned pads mean little visual or acoustic separation from neighbors; cars and voices are close.",
    "best_for": "Campers who accept a more urban-campground level of proximity in exchange for waterfalls and short hikes.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "full-shade", "very-close-sites", "waterfall-hikes", "cluster-level-only"]
  },
  "9": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (central, flatter pad)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Representative shaded creekside experience with a reasonably flat pad suitable for tents or small rigs; convenient to bathrooms and water.",
    "cons": "Still very close to other sites; generator and campfire noise from neighboring sites is common on busy weekends.",
    "best_for": "Families or pairs who want a straightforward, full-shade campsite and plan to spend much of the day on the waterfall trails.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "creekside", "full-shade", "rooftop-tent-friendly", "very-close-sites", "cluster-level-only"]
  },
  "10": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (central, flatter pad)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Short walk from the parking pad to tent area; good shade and proximity to restrooms and trailheads; flat enough for easy tent setup.",
    "cons": "No meaningful buffer from neighbors; road and other campsites feel very close by.",
    "best_for": "Short, low-effort family trips where being near everything matters more than privacy.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "full-shade", "rooftop-tent-friendly", "very-close-sites", "family-weekend-spot", "cluster-level-only"]
  },
  "11": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (mid-loop)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Typical Uvas configuration: heavily shaded site near the creek and bathrooms, with short walking distances to most amenities.",
    "cons": "Campsites here share the same tight spacing and low privacy as the rest of the loop; sound carries easily.",
    "best_for": "Campers okay with a compact, social campground as a base for hiking and waterfall viewing.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "full-shade", "very-close-sites", "waterfall-hikes", "cluster-level-only"]
  },
  "12": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (mid-loop, flatter pad)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Well-shaded mid-loop site with a relatively flat parking/tent pad, suitable for tents and rooftop tents; close to facilities and trails.",
    "cons": "Still tightly packed among other sites; expect typical weekend campground noise and limited seclusion.",
    "best_for": "Families and small groups who want simple logistics and a level pad more than extra space.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "full-shade", "rooftop-tent-friendly", "very-close-sites", "family-weekend-spot", "cluster-level-only"]
  },
  "13": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (mid-loop)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Easy, flat access from car to tent site in a fully shaded canyon environment; close to water and restrooms.",
    "cons": "Little to no visual privacy; other camps and vehicles are in clear view and earshot.",
    "best_for": "Campers who view Uvas as a comfortable overnight stop or waterfall base rather than a solitude destination.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "full-shade", "very-close-sites", "cluster-level-only"]
  },
  "14": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (inner row)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Deep shade, creek ambience, and short walking distances to all parts of the small campground.",
    "cons": "Inner-row feel with close neighbors on both sides and across the way; privacy is minimal.",
    "best_for": "Families or friend groups who are comfortable in a tight, social campground layout.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "full-shade", "very-close-sites", "social", "cluster-level-only"]
  },
  "15": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (inner row)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Same advantages as other Uvas sites: strong tree cover, easy access to restrooms, and quick jumps onto waterfall trails.",
    "cons": "Sound and light from neighboring camps are very noticeable due to close spacing and narrow canyon.",
    "best_for": "Groups or families who plan to spend much of their time on hikes and at the creek rather than at camp seeking quiet.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "full-shade", "very-close-sites", "waterfall-hikes", "cluster-level-only"]
  },
  "16": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (inner row)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Short distances to bathrooms, water, and trailheads; predictable, easy access similar to most sites in the loop.",
    "cons": "Aligned closely with neighboring pads; minimal separation or sense of personal space.",
    "best_for": "Campers who are used to busy state-park-style campgrounds and mainly want a reliable, shaded spot.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "full-shade", "very-close-sites", "cluster-level-only"]
  },
  "17": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (inner row)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Lush, shaded canyon setting with the same quick access to amenities as the rest of the campground.",
    "cons": "Typical Uvas spacing with little privacy; may feel crowded on peak weekends.",
    "best_for": "Families who value water features and shade over campsite seclusion.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "full-shade", "very-close-sites", "family-weekend-spot", "cluster-level-only"]
  },
  "18": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (inner row)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Heavily shaded site in a lush canyon, handy to restrooms and picnic areas.",
    "cons": "Very close to other sites and the narrow campground road; not suited for those seeking a quiet, secluded retreat.",
    "best_for": "Short, social camping trips with friends or family.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "full-shade", "very-close-sites", "social", "cluster-level-only"]
  },
  "19": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (inner row)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Shade, water sounds, and short access distances make it simple to manage with kids or mixed-experience campers.",
    "cons": "Same close spacing and limited privacy as the rest of Uvas; generator noise from small RVs is possible nearby.",
    "best_for": "Families comfortable with a close-knit campground scene.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "full-shade", "very-close-sites", "family-weekend-spot", "cluster-level-only"]
  },
  "20": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (toward loop end)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Near the end of the small loop, which can feel marginally less trafficked while still being close to restrooms and trails.",
    "cons": "Only a slight improvement at best; sites remain packed closely together.",
    "best_for": "Campers who want all of Uvas's conveniences and don’t expect true seclusion.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "full-shade", "very-close-sites", "cluster-level-only"]
  },
  "21": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (toward loop end)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Same waterfall access, shade, and short walking distances that characterize the whole campground.",
    "cons": "Limited separation from the restroom path and other sites; can see more traffic at busy times.",
    "best_for": "Campers unconcerned with traffic and proximity who value convenience most.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "full-shade", "very-close-sites", "near-restroom", "cluster-level-only"]
  },
  "22": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (toward loop end)",
    "privacy": 2,
    "shade": "Full",
    "pros": "Still enjoys the benefits of this small park: strong shade, clean bathrooms, and waterfall hiking close by.",
    "cons": "Tight layout and low privacy; you will hear and see nearby campers clearly.",
    "best_for": "Groups who are more interested in hanging out together than in having much distance from others.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "full-shade", "very-close-sites", "social", "cluster-level-only"]
  },
  "23": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (loop-end, relatively quieter)",
    "privacy": 3,
    "shade": "Full",
    "pros": "Near the end of the small loop, which can slightly reduce through-traffic and give a bit more quiet while still being close to trails and restrooms.",
    "cons": "Even here, spacing is tight and you should still expect to see and hear your neighbors.",
    "best_for": "Couples or small families trying to balance convenience with a modest step away from the busiest central row.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "end-of-loop", "full-shade", "moderate-privacy", "waterfall-hikes", "cluster-level-only"]
  },
  "24": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (loop-end, relatively quieter)",
    "privacy": 3,
    "shade": "Full",
    "pros": "Loop-end placement marginally reduces foot and vehicle traffic while preserving all the usual Uvas conveniences.",
    "cons": "Still not genuinely secluded; neighbors are just as close as elsewhere in the park.",
    "best_for": "Campers who want the Uvas experience but prefer not to be in the absolute middle of the activity.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "end-of-loop", "full-shade", "moderate-privacy", "cluster-level-only"]
  },
  "25": {
    "vibe": "Standard Uvas Canyon Tent/Car Site (loop-end, relatively quieter)",
    "privacy": 3,
    "shade": "Full",
    "pros": "Last site in a very small, shaded campground; slightly fewer people walking past your picnic table; same quick access to waterfalls.",
    "cons": "Privacy gain is modest; close proximity to neighbors and road remains a defining trait.",
    "best_for": "Couples or small groups who want a tiny bit more breathing room while still embracing the social, compact nature of Uvas.",
    "tags": ["standard-car-camping", "tent-or-small-rv", "end-of-loop", "full-shade", "moderate-privacy", "waterfall-hikes", "cluster-level-only"]
  }
}
}