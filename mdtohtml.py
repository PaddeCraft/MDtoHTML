import markdown

md = markdown.Markdown(extensions=["codehilite"])

def replace(replin):
    rpin = replin
    rpin = rpin.replace("Ã¤", "ä")
    rpin = rpin.replace("Ã¶", "ö")
    rpin = rpin.replace("Ã¼", "ü")
    rpin = rpin.replace("Ã„", "Ä")
    rpin = rpin.replace("Ã–", "Ö")
    rpin = rpin.replace("Ãœ", "Ü")
    rpin = rpin.replace("ÃŸ", "ß")
    rpin = rpin.replace("Â§", "§")
    rpin = rpin.replace("Â°", "°")
    rpin = rpin.replace("ðŸ˜Ž", "😎")
    rpin = rpin.replace("cookie", "😸")
    rpin = rpin.replace("mogli", "🐱‍👤")
    if "[yt]" in rpin.lower() and "[yt]" in rpin.split(" ")[0].lower():
        rpin = f'<iframe width="{rpin.split(" ")[2]}" height="{rpin.split(" ")[3]}" src="https://www.youtube.com/embed/{rpin.split(" ")[1]}"></iframe>'
    return rpin

# css: "dark", "light","None", <path> or <url>
def mdtohtml(markdownin, title="", css="dark", cssinhtml="False"):
    finishedHtml = ""
    html = []
    for mdline in list(markdownin):
        html.append(replace(md.reset().convert(mdline)))
    for item in html:
        finishedHtml = f"{finishedHtml}\n{item}"
    if not title == "":
        finishedHtml = f"{finishedHtml}\n<title>{title}</title>"
    return finishedHtml