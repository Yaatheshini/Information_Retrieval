'''
Generalizes the output of print_document.py from documents 1-20 of CISI
'''

import random
import subprocess

print("Testing output of print_document -- expected to PASS")
correct_documents = {}

correct_documents["1"] = "   The present study is a history of the DEWEY Decimal" \
" Classification.  The first edition of the DDC was published" \
" in 1876, the eighteenth edition in 1971, and future editions" \
" will continue to appear as needed.  In spite of the DDC's" \
" long and healthy life, however, its full story has never" \
" been told.  There have been biographies of Dewey" \
" that briefly describe his system, but this is the first" \
" attempt to provide a detailed history of the work that" \
" more than any other has spurred the growth of" \
" librarianship in this country and abroad. "

correct_documents["2"] = "This report is an analysis of 6300 acts of use" \
" in 104 technical libraries in the United Kingdom." \
" Library use is only one aspect of the wider pattern of" \
" information use.  Information transfer in libraries is" \
" restricted to the use of documents.  It takes no" \
" account of documents used outside the library, still" \
" less of information transferred orally from person" \
" to person.  The library acts as a channel in only a" \
" proportion of the situations in which information is" \
" transferred." \
" Taking technical information transfer as a whole," \
" there is no doubt that this proportion is not the" \
" major one.  There are users of technical information -" \
" particularly in technology rather than science -" \
" who visit libraries rarely if at all, relying on desk" \
" collections of handbooks, current periodicals and personal" \
" contact with their colleagues and with people in other" \
" organizations.  Even regular library users also receive" \
" information in other ways."

correct_documents["3"] = "    The relationships between the organization and control of writings" \
" and the organization and control of knowledge and information will" \
" inevitably enter our story, for writings contain, along with much else, a" \
" great deal of mankind's stock of knowledge and information.  Bibliographical" \
" control is a form of power, and if knowledge itself is a form of power," \
" as the familiar slogan claims, bibliographical control is in a certain sense" \
" power over power, power to obtain the knowledge recorded in written" \
" form.  As writings are not simply, and not in any simple way, storehouses of" \
" knowledge, we cannot satisfactorily discuss bibliographical control as" \
" simply control over the knowledge and information contained in writings." 

correct_documents["4"] = "    The establishment of nine new universities in the 1960's provoked a highly" \
" stimulating re-examination of the nature, purpose and management of academic" \
" libraries.  Long-established attitudes and methods were questioned, but" \
" although changes were made, the basic difficulty remained - a lack of objective" \
" information about the best ways of providing a library service in a university." \
" The report of the UGC Committee on Libraries (the Parry Repot [267]), which," \
" in general, endorsed these changes, also stressed the need for research into" \
" all aspects of academic library provision." 

correct_documents["5"] = "    Although the use of games in professional education has" \
" become widespread only during the last decade, the method has" \
" been used in a number of fields for many hundreds of years." \
" Its origins have been traced to simple war games, used in" \
" military training when the \"real thing\" was either unavailable" \
" or too dangerous.  In more recent times, these games have" \
" become more and more sophisticated, and many now use large" \
" electronic computers to handle the complex calculations involved." \
" Since 1956, when the first well-developed management game was" \
" introduced, the technique has spread rapidly into a wide variety" \
" of disciplines and today it is used at all levels of education," \
" from primary school classes to courses for experienced professional" \
" men and women.  One of the main causes of this \"game explosion\"" \
" has been the rapid development of sophisticated management" \
" techniques, such as simulation and mathematical modelling, which" \
" have been made possible by rapid advances in computer technology."

correct_documents["6"] = "     Graduate library school study of abstracting should be more than a" \
" how-to-do-it course." \
" It should include general material on the characteristcs and types of abstracts," \
" the historical development of abstracting publications, the abstract-publishing" \
" industry (especially in the United States), and the need for standards in the" \
" preparation and evaluation of the product." \
" These topics we call concepts." \
"      The text includes a methods section containing instructions for writing" \
" various types of abstracts, and for editing and preparing abstracting publications." \
" These detailed instructions are supplemented by examples and exercises in the" \
" appendix." \
" There is a brief discussion of indexing of abstract publications." \
"      Research on automation has been treated extensively in this work, for we" \
" believe that the topic deserves greater emphasis than it has received in the" \
" past." \
" Computer use is becoming increasingly important in all aspects of librarianship." \
" Much research effort has been expended on the preparation and evaluation of" \
" computer-prepared abstracts and extracts." \
" Students, librarians, and abstractors will benefit from knowing about this" \
" research and understanding how computer programs were researched to analyze text," \
" select key sentences, and prepare extracts and abstracts." \
" The benefits of this research are discussed." \
"    Abstracting is a key segment of the information industry." \
" Opportunities are available for both full-time professionals and part-time or" \
" volunteer workers." \
" Many librarians find such activities pleasant and rewarding, for they know" \
" they are contributing to the more effective use of stored information." \
" One chapter is devoted to career opportunities for abstractors." 

correct_documents["7"] = "This book attempts to present representative examples of successful" \
" architectural solutions to the important problems librarians and" \
" architects face in planning new college and university library" \
" buildings or in remodeling and enlarging existing structures.  It does" \
" not attempt to make case study evaluations, as was done by" \
" Ellsworth Mason for Brown and Yale.  Nor does it present examples" \
" of unsuccessful solutions except to show how to avoid mistakes," \
" and in these cases the libraries will not be identified." \

correct_documents["8"] = "     As important for staff members' individual development" \
" as was the apprenticeship in administration, perhaps the most" \
" significant attitude one acquired while working for" \
" Guy was engendered by his insistence that librarians must" \
" be interested in and knowledgeable about the content of the" \
" materials with which they dealt.  His love of literature, his" \
" respect for scholarship, his admiration for good writing and" \
" reading were manifested in many ways, but most notably in" \
" his admonition that, though we were primarily a research" \
" library, we must constantly keep in mind our obligation to" \
" collect contemporary poetry, fiction and belles-letters.  It" \
" was primarily up to the library staff, he felt, to be" \
" responsible for these as well as for \"general\" books which crossed" \
" disciplinary lines or fell between the disciplines, those books" \
" which a faculty mostly concerned with research materials is" \
" apt to overlook.  And in building this portion of the collection," \
" \"there is no substitute for a thorough acquaintance with" \
" books through a reading of critical reviews and the books" \
" themselves.\"  This counsel is from The President, the Professor," \
" and the College Library, but the importance of its thrust--the" \
" need to keep up with the world of books and publishing--was" \
" continually impressed upon us."

correct_documents["9"] = "     This study assumed that an additional use study held" \
" less promise than an analytical consideration of concepts." \
" The basic approach was a survey comparing traditional and" \
" current professional ideas on direct access.  Principal data-gathering" \
" instruments were documentary analysis and opinion questionnaire." \
"      Findings of the documentary analysis included the following:" \
"      Research from 1890 to 1970 on the direct shelf approach" \
" and browsing left the problems largely unresolved and" \
" evidently resistant to established methods of use and user" \
" research.  The need for an exhaustive study of concepts was" \
" confirmed." \
"      Open shelf libraries--organized through shelf classification" \
" and relative location--were meant to arouse the intellectual," \
" social, and political interest of the average citizen and affect" \
" his democratic self-realization." \
"      Definitions of \"browsing\" varied greatly: self-indulgence" \
" by the untutored in objectionable works; beneficial self-education" \
" for the general reader; valuable guidance for the scholar in his" \
" research." 

correct_documents["10"] = "          The purpose of this study was to develop, evaluate," \
" and recommend a national plan  for improving access to periodical" \
" resources.  About 48 percent of all academic interlibrary loans" \
" are for periodical materials, with the bulk of the loans being" \
" satisfied in the form of photocopies.  A major consideration in" \
" the long-range improvement of the interlibrary loan system is" \
" the possible augmentation with a national system for acquiring," \
" storing, and satisfying loan requests for periodical materials." \
"           This study focused on the physical access to the" \
" periodical literature.  Based on the needs of the library community," \
" design features were developed, and included the following:" \
"           Service should be made available to all users" \
"           without any restriction other than access" \
"           through a library." \
"           Initially, the service should be confined primarily" \
"           to rapid, dependable delivery of photocopies of" \
"           journal articles." \
"           The collection of a center should be comprehensive" \
"           in subject coverage excluding only medicine." \
"           All worthwhile journals should be collected" \
"           irrespective of language."

correct_documents["11"] = "  The scope of acquisitions work, outlined in the Introduction," \
" acknowledges the importance of selection policy," \
" serials recording, and other topics kindred to acquisitions." \
" These topics are discussed in this book only as they relate" \
" to obtaining library materials.  They are examined thoroughly" \
" in books and papers that are cited in the references and the" \
" bibliographic note." \
"   Centralized acquisitions and automation of order routines are of" \
" major importance in order work and they are reviewed as chapters in" \
" this book.  These chapters are introductions to the concepts and" \
" problems of centralization and automation, not manuals of practice." \
" For treatment of these topics in particular and in depth the reader is" \
" referred to the references cited.  For automation these references" \
" are only a modest selection from an enormous literature."

correct_documents["12"] = "  The Ligue des bibliotheques europeennes de recherche (LIBER) was set up" \
" in 1971 as an international non-governmental organization, with the aim of" \
" establishing close collaboration between the general research libraries of" \
" Western Europe, particularly national and university libraries, and in" \
" particular to help in finding practical ways of improving the quality of" \
" the services these libraries provide." \
"   At the second meeting of its General Assembly, held in Luxembourg in 1972," \
" LIBER decided to hold a seminar on the acquisition of materials from the" \
" 'Third World'; and I was charged with the 'intellectual organization' of this" \
" seminar.  The purpose of the meeting would be to examine the problems of" \
" acquisition; the availability of materials in European libraries both for" \
" reference and for lending; and the feasibility of setting up a European centre" \
" for the collection of such material, to be available for loan.  The provision" \
" of bibliographic information, preferable in machine-readable form, was to be" \
" a basic consideration, whatever means were proposed for acquiring publications" \
" from those areas.  The Council of Europe made a generous grant towards the" \
" cost of the seminar which was held at the University of Sussex from 17 to 19" \
" September 1973."

correct_documents["13"] = "I am not, nor have I ever pretended to be, an expert on" \
" microfiche.  Nevertheless, when I was invited to address the" \
" Third Annual Northeastern DDC/Industry Users Conference in" \
" Waltham, Massachusetts in April of 1968 I had the temerity to" \
" attempt to describe what I as a user would like to have in a" \
" fiche reader.  (\"Towards a Uniform Federal Report Numbering" \
" System and a Cuddly Microfiche Reader--Two Modest Proposals.\""\
" Revised September 1968.  AD-669204)"

correct_documents["14"] = "  If this book has a central thesis, it rests upon the simple but" \
" frequently neglected principle that college library service goes" \
" beyond the commonly accepted functions of book circulation and" \
" storage.  The college library exists, not merely to house and" \
" circulate library materials, but to supplement and extend the teaching" \
" process with reference service, to afford faculty members library" \
" opportunities for improving instruction, and to encourage students" \
" to read more and better books.  Administration is essentially a" \
" service activity, a tool through which library functions are more" \
" fully and efficiently realized." \
"   The present work retains most of the material of the first edition," \
" but includes substantial revision in each chapter.  The book was" \
" planned not only as a text in the teaching of college library" \
" administration but also for independent professional reading.  Because" \
" readers have found the footnotes and chapter bibliographies useful" \
" for reference purposes, they have been brought up to date and in" \
" some cases extended."

correct_documents["15"] = "   Technical communication patterns in two research and development laboratories" \
" were examined using modified sociometric techniques.. The structure of " \
" technical communication networks in the two laboratories results from the" \
" interaction of both social relations and work structure.. The sociometric " \
" \"stars\" in the technical communication network who provide other members of the" \
" organization with information either make greater use of individuals outside" \
" the organization or read the literature more than other members of the " \
" laboratory.."

correct_documents["16"] = "     This manual is designed to make it possible for any library to change" \
" efficiently to the Library of Congress Classification system.  Detailed" \
" procedures are outlined which may serve as exact models or as a series of" \
" suggested steps which have proven effective in actual use.  Most of the text" \
" deals with the necessary criteria for effecting the planning, making the" \
" preparations, selecting the tools, and establishing the procedures which" \
" are essential for a reclassification project.  Beyond this, considerable" \
" attention has been given to many of the problem areas of the LC" \
" Classification-series, biography, bibliography, law, PZ3 and PZ4.  In" \
" addition, the literature Tables VIIIa and IXa, two of the most" \
" frequently used tables throughout the entire class system, have been" \
" thoroughly explained and their application illustrated by a series of" \
" comprehensive examples.  Since the mechanics, production, and cost of" \
" catalogue card copy can significantly affect the flow of books to users," \
" a chapter has been devoted to describing the use of Xerox copying" \
" machines in library operations.  Finally, an annotated bibliography" \
" of books and articles judged to be helpful in deciding to reclassify is" \
" included for those readers who wish to delve more deeply into the" \
" tortuous and frustrating 50-year history of the concept of centralized" \
" cataloging and classification.  The numbers enclosed in parentheses" \
" throughout the text refer to sources in the bibliography which relate" \
" to or support the arguments being advanced in any particular case."

correct_documents["17"] = "  There has long been a need for a continuing series to provide" \
" scholarly reviews of the rapidly changing and advancing field of" \
" librarianship, a series which would select subjects with particular" \
" current significance to the profession and provide an analysis of" \
" the advances made through research and practice.  Advances in" \
" Librarianship is planned and designed to fill this need.  It will" \
" present critical articles and surveys based on the published literature," \
" research in progress, and developments in libraries of all types." \
"    Mechanization may appear to be the most obvious of the advancing fronts" \
" of librarianship, for automation has caught the enthusiastic support of all" \
" librarians who can visualize its potential." \
" Advances in this field will certainly be found in every volume of this series." \
" As the first group of articles in this volume demonstrate, technological change" \
" has an obvious and direct implication for libraries, but the problem has been" \
" found to be much more complex than the simple inventory problem many experts" \
" expected." \
" Advances in Librarianship is dedicated to presenting the realities of" \
" automation, assessing where we are, where we are going, and how fast we can hope" \
" to get there." \
" \"The Machine and Cataloging\" reviews the current status of the machine-produced" \
" book catalog and what lies ahead as we enter the age of MARC." \
" Where business methods have greater applicability, progress is easier, as" \
" reported in \"Mechanization of Acquisition Processes.\"" \
" Even in this area generally acceptable practices and standardization are in the" \
" future, not the past." \
" One of the problems of major and immediate importance in computerization of" \
" catalog information is that discussed in \"Filing Systems for Computer" \
" Manipulation.\"" \
" This detailed review presents the complexity of the problems and suggests" \
" possible solutions." \
"    For many years technical service costs have been defended without adequate" \
" knowledge of the facts." \
" As automated procedures are proposed, standards are determining costs of" \
" traditional operations become essential." \
" The article on standards for such costs shows why the problems have been difficult" \
" and reviews the significant advances of the past few years." \
"    The school library has widened its dimensions in materials and services much" \
" more rapidly than other libraries, as reflected in its new name, the" \
" instructional media center." \
" Here, technical change, together with new teaching methods, has made possible" \
" major developments in library service in schools as well as for children in" \
" the public library." \
" Two articles make clear that what can be done has been demonstrated, and that" \
" what remains is to make this the rule rather than the exception." \
"    Bibliotherapy is an example of a field in which progress has been slow." \
"    Articles which illustrate the potential which systems theory and managerial" \
" planning theory have for libraries." \
" The articles on the application of these concepts, which come from research in" \
" administration, are provocative and may appear controversial to some." \
"    The article on library development in developing countries provides an" \
" analysis in depth of our efforts and degree of success in assisting other" \
" countries in providing the library service which is so important in the modern" \
" world."

correct_documents["18"] = "  The present contribution does not duplicate previous studies but" \
" complements the earlier publications and closes the few gaps that" \
" exist in the literature prior to 1966 and after 1971.  Additionally," \
" it is a bold attempt to evaluate critically and objectively the history" \
" of the mechanized selective dissemination of information (SDI) as" \
" reflected in the literature, from the initial description by Luhn" \
" (1958, 1961b, c) to the post-1970 period when the SDI boom began losing" \
" ground to the more popular on-line interactive systems.  The review" \
" therefore questions and interprets the concept of SDI, its implementation," \
" and its evolution in the light of work performed by many companies," \
" government agencies, universities, societies, and libraries during the" \
" last fourteen years."

correct_documents["19"] = "  In trying to give an account of the statistical properties of" \
" language, one is faced with the problem of having to find the" \
" common thread which would show the many and multifarious forms" \
" of language statistics - embodied in scattered papers written" \
" by linguists, philosophers, mathematicians, engineers, each using" \
" his own professional idiom as belonging to one great whole:" \
" quantitative linguistics." \
"   The book stresses the peculiarity of statistics of language" \
" structure as against just conventional statistics.  To put the" \
" difference between two types of statistics briefly, the latter comprises" \
" the methods and parameters of general number statistics as applied, e.g., in" \
" Economics and Demography, the former has its own methods and characterising" \
" parameters, particularly useful for describing and evaluating language" \
" structure.  The idea of statistical linguistics as using concepts and" \
" methods of its own, which was adumbrated in the author's \"Language as" \
" choice and Chance\", 1956, has now taken definite shape." \
"   Of this development I shall try to give a brief account.  In my book," \
" \"Language as Choice and Chance\", the foundation was laid for a truly" \
" sensible application of statistics to language by my interpretation" \
" of the langue-parole dichotomy as being essentially that between statistical" \
" universe and sample."

correct_documents["20"] = "     Most librarians mark the beginning of modern librarianship" \
" from the founding of the American Library Association in 1876 and" \
" the appearance on the national library scene of such dynamic and" \
" controversial figures as Melvil Dewey and Charles Ammi Cutter." \
"      But in doing so, they overlook an extremely significant era in" \
" the history of our profession, for the quarter century preceding the" \
" 1876 meeting in Philadelphia was one characterized by great advances" \
" in the field of American librarianship.  This period of growth was to" \
" have considerable influence on the course of library development in" \
" America after 1876.  To ignore the third quarter of the nineteenth" \
" century is to risk misinterpreting the pivotal post-1876 era," \
" and in this time of reappraisal, it seems particularly appropriate" \
" and useful to focus our attention on the years preceding the founding" \
" of the American Library Association."

program = "./code/print_document.py"
collection = "CISI"
docID = str(random.randint(1, 20))

print("Document generated is: ", docID)

output = subprocess.check_output(["python3", program, collection, docID])
answer = output.decode('utf-8').strip()

# compare outputs, word by word
words_answer = answer.split()
words_doc = correct_documents[docID].strip().split()

if len(words_doc) == len(words_answer):
    for i in range(len(words_answer)):
        if words_doc[i] != words_answer[i]:
            print("FAIL: The text words don't match.")
            exit(1) # signal error to OS

    # if we reach this point, the answer is correct
    print("PASS")
    exit(0) # signal success to OS

# if we reach this point, the returned document is not as expected
print("FAIL: The number of words in the text doesn't match.")
exit(1) # signal error to OS
