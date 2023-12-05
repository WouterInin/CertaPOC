# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 13:04:37 2023

@author: WouterMuldersinin
"""
import streamlit as st
import pandas as pd
#import time
#import streamlit as st
import random
from bs4 import BeautifulSoup 
#from htmldocx import HtmlToDocx
#from docx import Document
#import pdfplumber
#import pdfgen
#import pdfkit
#new_parser = HtmlToDocx()


basis_html = """<html xmlns:v="urn:schemas-microsoft-com:vml"
xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:w="urn:schemas-microsoft-com:office:word"
xmlns:m="http://schemas.microsoft.com/office/2004/12/omml"
xmlns="http://www.w3.org/TR/REC-html40">

<head>
<meta http-equiv=Content-Type content="text/html; charset=windows-1252">
<meta name=ProgId content=Word.Document>
<meta name=Generator content="Microsoft Word 15">
<meta name=Originator content="Microsoft Word 15">
<link rel=File-List
href="Voorbeeld_vast_contract%20-%20kopie_bestanden/filelist.xml">
<title>Model arbeidsovereenkomst voor onbepaalde tijd</title>
<!--[if gte mso 9]><xml>
 <o:DocumentProperties>
  <o:Author>Magda Lacroes-Felesita</o:Author>
  <o:Template>Normal</o:Template>
  <o:LastAuthor>Wouter Mulders | inin</o:LastAuthor>
  <o:Revision>2</o:Revision>
  <o:TotalTime>0</o:TotalTime>
  <o:Created>2023-11-15T15:03:00Z</o:Created>
  <o:LastSaved>2023-11-15T15:03:00Z</o:LastSaved>
  <o:Pages>3</o:Pages>
  <o:Words>638</o:Words>
  <o:Characters>3510</o:Characters>
  <o:Company>CWI</o:Company>
  <o:Lines>29</o:Lines>
  <o:Paragraphs>8</o:Paragraphs>
  <o:CharactersWithSpaces>4140</o:CharactersWithSpaces>
  <o:Version>16.00</o:Version>
 </o:DocumentProperties>
 <o:OfficeDocumentSettings>
  <o:TargetScreenSize>800x600</o:TargetScreenSize>
 </o:OfficeDocumentSettings>
</xml><![endif]-->
<link rel=themeData
href="Voorbeeld_vast_contract%20-%20kopie_bestanden/themedata.thmx">
<link rel=colorSchemeMapping
href="Voorbeeld_vast_contract%20-%20kopie_bestanden/colorschememapping.xml">
<!--[if gte mso 9]><xml>
 <w:WordDocument>
  <w:SpellingState>Clean</w:SpellingState>
  <w:GrammarState>Clean</w:GrammarState>
  <w:TrackMoves>false</w:TrackMoves>
  <w:TrackFormatting/>
  <w:HyphenationZone>21</w:HyphenationZone>
  <w:PunctuationKerning/>
  <w:ValidateAgainstSchemas/>
  <w:SaveIfXMLInvalid>false</w:SaveIfXMLInvalid>
  <w:IgnoreMixedContent>false</w:IgnoreMixedContent>
  <w:AlwaysShowPlaceholderText>false</w:AlwaysShowPlaceholderText>
  <w:DoNotPromoteQF/>
  <w:LidThemeOther>NL</w:LidThemeOther>
  <w:LidThemeAsian>X-NONE</w:LidThemeAsian>
  <w:LidThemeComplexScript>X-NONE</w:LidThemeComplexScript>
  <w:Compatibility>
   <w:BreakWrappedTables/>
   <w:SnapToGridInCell/>
   <w:WrapTextWithPunct/>
   <w:UseAsianBreakRules/>
   <w:UseWord2010TableStyleRules/>
   <w:DontGrowAutofit/>
   <w:DontUseIndentAsNumberingTabStop/>
   <w:FELineBreak11/>
   <w:WW11IndentRules/>
   <w:DontAutofitConstrainedTables/>
   <w:AutofitLikeWW11/>
   <w:HangulWidthLikeWW11/>
   <w:UseNormalStyleForList/>
   <w:DontVertAlignCellWithSp/>
   <w:DontBreakConstrainedForcedTables/>
   <w:DontVertAlignInTxbx/>
   <w:Word11KerningPairs/>
   <w:CachedColBalance/>
  </w:Compatibility>
  <w:BrowserLevel>MicrosoftInternetExplorer4</w:BrowserLevel>
  <m:mathPr>
   <m:mathFont m:val="Cambria Math"/>
   <m:brkBin m:val="before"/>
   <m:brkBinSub m:val="&#45;-"/>
   <m:smallFrac m:val="off"/>
   <m:dispDef/>
   <m:lMargin m:val="0"/>
   <m:rMargin m:val="0"/>
   <m:defJc m:val="centerGroup"/>
   <m:wrapIndent m:val="1440"/>
   <m:intLim m:val="subSup"/>
   <m:naryLim m:val="undOvr"/>
  </m:mathPr></w:WordDocument>
</xml><![endif]--><!--[if gte mso 9]><xml>
 <w:LatentStyles DefLockedState="false" DefUnhideWhenUsed="false"
  DefSemiHidden="false" DefQFormat="false" LatentStyleCount="376">
  <w:LsdException Locked="false" QFormat="true" Name="Normal"/>
  <w:LsdException Locked="false" QFormat="true" Name="heading 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   QFormat="true" Name="heading 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   QFormat="true" Name="heading 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   QFormat="true" Name="heading 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   QFormat="true" Name="heading 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   QFormat="true" Name="heading 6"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   QFormat="true" Name="heading 7"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   QFormat="true" Name="heading 8"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   QFormat="true" Name="heading 9"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   QFormat="true" Name="caption"/>
  <w:LsdException Locked="false" QFormat="true" Name="Title"/>
  <w:LsdException Locked="false" QFormat="true" Name="Subtitle"/>
  <w:LsdException Locked="false" QFormat="true" Name="Strong"/>
  <w:LsdException Locked="false" QFormat="true" Name="Emphasis"/>
  <w:LsdException Locked="false" Priority="99" SemiHidden="true"
   Name="Placeholder Text"/>
  <w:LsdException Locked="false" Priority="1" QFormat="true" Name="No Spacing"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 1"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 1"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 1"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 1"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 1"/>
  <w:LsdException Locked="false" Priority="99" SemiHidden="true" Name="Revision"/>
  <w:LsdException Locked="false" Priority="34" QFormat="true"
   Name="List Paragraph"/>
  <w:LsdException Locked="false" Priority="29" QFormat="true" Name="Quote"/>
  <w:LsdException Locked="false" Priority="30" QFormat="true"
   Name="Intense Quote"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 1"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 1"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 1"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 1"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 1"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 1"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 2"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 2"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 2"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 2"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 2"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 2"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 2"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 2"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 2"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 2"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 2"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 3"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 3"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 3"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 3"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 3"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 3"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 3"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 3"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 3"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 3"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 3"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 4"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 4"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 4"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 4"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 4"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 4"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 4"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 4"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 4"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 4"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 4"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 5"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 5"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 5"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 5"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 5"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 5"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 5"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 5"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 5"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 5"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 5"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 6"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 6"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 6"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 6"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 6"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 6"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 6"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 6"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 6"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 6"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 6"/>
  <w:LsdException Locked="false" Priority="19" QFormat="true"
   Name="Subtle Emphasis"/>
  <w:LsdException Locked="false" Priority="21" QFormat="true"
   Name="Intense Emphasis"/>
  <w:LsdException Locked="false" Priority="31" QFormat="true"
   Name="Subtle Reference"/>
  <w:LsdException Locked="false" Priority="32" QFormat="true"
   Name="Intense Reference"/>
  <w:LsdException Locked="false" Priority="33" QFormat="true" Name="Book Title"/>
  <w:LsdException Locked="false" Priority="37" SemiHidden="true"
   UnhideWhenUsed="true" Name="Bibliography"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="TOC Heading"/>
  <w:LsdException Locked="false" Priority="41" Name="Plain Table 1"/>
  <w:LsdException Locked="false" Priority="42" Name="Plain Table 2"/>
  <w:LsdException Locked="false" Priority="43" Name="Plain Table 3"/>
  <w:LsdException Locked="false" Priority="44" Name="Plain Table 4"/>
  <w:LsdException Locked="false" Priority="45" Name="Plain Table 5"/>
  <w:LsdException Locked="false" Priority="40" Name="Grid Table Light"/>
  <w:LsdException Locked="false" Priority="46" Name="Grid Table 1 Light"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark"/>
  <w:LsdException Locked="false" Priority="51" Name="Grid Table 6 Colorful"/>
  <w:LsdException Locked="false" Priority="52" Name="Grid Table 7 Colorful"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 1"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 1"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 1"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 1"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 1"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 1"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 2"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 2"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 2"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 2"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 2"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 2"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 3"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 3"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 3"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 3"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 3"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 3"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 4"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 4"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 4"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 4"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 4"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 4"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 5"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 5"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 5"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 5"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 5"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 5"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 6"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 6"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 6"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 6"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 6"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 6"/>
  <w:LsdException Locked="false" Priority="46" Name="List Table 1 Light"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark"/>
  <w:LsdException Locked="false" Priority="51" Name="List Table 6 Colorful"/>
  <w:LsdException Locked="false" Priority="52" Name="List Table 7 Colorful"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 1"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 1"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 1"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 1"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 1"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 1"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 2"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 2"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 2"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 2"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 2"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 2"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 3"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 3"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 3"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 3"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 3"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 3"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 4"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 4"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 4"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 4"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 4"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 4"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 5"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 5"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 5"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 5"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 5"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 5"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 6"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 6"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 6"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 6"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 6"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 6"/>
  <w:LsdException Locked="false" Priority="99" SemiHidden="true"
   UnhideWhenUsed="true" Name="Mention"/>
  <w:LsdException Locked="false" Priority="99" SemiHidden="true"
   UnhideWhenUsed="true" Name="Smart Hyperlink"/>
  <w:LsdException Locked="false" Priority="99" SemiHidden="true"
   UnhideWhenUsed="true" Name="Hashtag"/>
  <w:LsdException Locked="false" Priority="99" SemiHidden="true"
   UnhideWhenUsed="true" Name="Unresolved Mention"/>
  <w:LsdException Locked="false" Priority="99" SemiHidden="true"
   UnhideWhenUsed="true" Name="Smart Link"/>
 </w:LatentStyles>
</xml><![endif]-->
<style>
<!--
 /* Font Definitions */
 @font-face
	{font-family:Wingdings;
	panose-1:5 0 0 0 0 0 0 0 0 0;
	mso-font-charset:2;
	mso-generic-font-family:auto;
	mso-font-pitch:variable;
	mso-font-signature:0 268435456 0 0 -2147483648 0;}
@font-face
	{font-family:"Cambria Math";
	panose-1:2 4 5 3 5 4 6 3 2 4;
	mso-font-charset:0;
	mso-generic-font-family:roman;
	mso-font-pitch:variable;
	mso-font-signature:-536869121 1107305727 33554432 0 415 0;}
@font-face
	{font-family:Verdana;
	panose-1:2 11 6 4 3 5 4 4 2 4;
	mso-font-charset:0;
	mso-generic-font-family:swiss;
	mso-font-pitch:variable;
	mso-font-signature:-1610610945 1073750107 16 0 415 0;}
@font-face
	{font-family:Tahoma;
	panose-1:2 11 6 4 3 5 4 4 2 4;
	mso-font-charset:0;
	mso-generic-font-family:swiss;
	mso-font-pitch:variable;
	mso-font-signature:-520081665 -1073717157 41 0 66047 0;}
 /* Style Definitions */
 p.MsoNormal, li.MsoNormal, div.MsoNormal
	{mso-style-unhide:no;
	mso-style-qformat:yes;
	mso-style-parent:"";
	margin:0cm;
	mso-pagination:widow-orphan;
	font-size:12.0pt;
	font-family:"Times New Roman",serif;
	mso-fareast-font-family:"Times New Roman";}
p.MsoCommentText, li.MsoCommentText, div.MsoCommentText
	{mso-style-unhide:no;
	mso-style-link:"Tekst opmerking Char";
	margin:0cm;
	mso-pagination:widow-orphan;
	font-size:10.0pt;
	font-family:"Times New Roman",serif;
	mso-fareast-font-family:"Times New Roman";}
span.MsoCommentReference
	{mso-style-unhide:no;
	mso-style-parent:"";
	mso-ansi-font-size:8.0pt;
	mso-bidi-font-size:8.0pt;}
p.MsoCommentSubject, li.MsoCommentSubject, div.MsoCommentSubject
	{mso-style-unhide:no;
	mso-style-parent:"Tekst opmerking";
	mso-style-link:"Onderwerp van opmerking Char";
	mso-style-next:"Tekst opmerking";
	margin:0cm;
	mso-pagination:widow-orphan;
	font-size:10.0pt;
	font-family:"Times New Roman",serif;
	mso-fareast-font-family:"Times New Roman";
	font-weight:bold;}
p.MsoAcetate, li.MsoAcetate, div.MsoAcetate
	{mso-style-unhide:no;
	mso-style-link:"Ballontekst Char";
	margin:0cm;
	mso-pagination:widow-orphan;
	font-size:8.0pt;
	font-family:"Tahoma",sans-serif;
	mso-fareast-font-family:"Times New Roman";}
p.Default, li.Default, div.Default
	{mso-style-name:Default;
	mso-style-unhide:no;
	mso-style-parent:"";
	margin:0cm;
	mso-pagination:widow-orphan;
	mso-layout-grid-align:none;
	text-autospace:none;
	font-size:12.0pt;
	font-family:"Verdana",sans-serif;
	mso-fareast-font-family:"Times New Roman";
	mso-bidi-font-family:Verdana;
	color:black;}
span.TekstopmerkingChar
	{mso-style-name:"Tekst opmerking Char";
	mso-style-unhide:no;
	mso-style-locked:yes;
	mso-style-link:"Tekst opmerking";}
span.OnderwerpvanopmerkingChar
	{mso-style-name:"Onderwerp van opmerking Char";
	mso-style-unhide:no;
	mso-style-locked:yes;
	mso-style-parent:"";
	mso-style-link:"Onderwerp van opmerking";
	font-weight:bold;}
span.BallontekstChar
	{mso-style-name:"Ballontekst Char";
	mso-style-unhide:no;
	mso-style-locked:yes;
	mso-style-parent:"";
	mso-style-link:Ballontekst;
	mso-ansi-font-size:8.0pt;
	mso-bidi-font-size:8.0pt;
	font-family:"Tahoma",sans-serif;
	mso-ascii-font-family:Tahoma;
	mso-hansi-font-family:Tahoma;
	mso-bidi-font-family:Tahoma;}
span.SpellE
	{mso-style-name:"";
	mso-spl-e:yes;}
.MsoChpDefault
	{mso-style-type:export-only;
	mso-default-props:yes;}
@page WordSection1
	{size:595.3pt 841.9pt;
	margin:72.0pt 90.0pt 72.0pt 90.0pt;
	mso-header-margin:35.4pt;
	mso-footer-margin:35.4pt;
	mso-paper-source:0;}
div.WordSection1
	{page:WordSection1;}
 /* List Definitions */
 @list l0
	{mso-list-id:52120904;
	mso-list-type:hybrid;
	mso-list-template-ids:352233560 68354051 68354051 68354053 68354049 68354051 68354053 68354049 68354051 68354053;}
@list l0:level1
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:36.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l0:level2
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:72.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l0:level3
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:108.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l0:level4
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:144.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l0:level5
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:180.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l0:level6
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:216.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l0:level7
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:252.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l0:level8
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:288.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l0:level9
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:324.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l1
	{mso-list-id:92482038;
	mso-list-type:hybrid;
	mso-list-template-ids:527603906 68354051 68354051 68354053 68354049 68354051 68354053 68354049 68354051 68354053;}
@list l1:level1
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:36.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l1:level2
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:72.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l1:level3
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:108.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l1:level4
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:144.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l1:level5
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:180.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l1:level6
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:216.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l1:level7
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:252.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l1:level8
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:288.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l1:level9
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:324.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l2
	{mso-list-id:535503388;
	mso-list-type:hybrid;
	mso-list-template-ids:-1511201858 68354049 68354051 68354053 68354049 68354051 68354053 68354049 68354051 68354053;}
@list l2:level1
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:36.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l2:level2
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:72.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l2:level3
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:108.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l2:level4
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:144.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l2:level5
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:180.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l2:level6
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:216.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l2:level7
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:252.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l2:level8
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:288.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l2:level9
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:324.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l3
	{mso-list-id:725496975;
	mso-list-type:hybrid;
	mso-list-template-ids:731524644 68354049 68354051 68354053 68354049 68354051 68354053 68354049 68354051 68354053;}
@list l3:level1
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:36.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l3:level2
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:72.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l3:level3
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:108.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l3:level4
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:144.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l3:level5
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:180.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l3:level6
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:216.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l3:level7
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:252.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l3:level8
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:288.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l3:level9
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:324.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l4
	{mso-list-id:902720335;
	mso-list-type:hybrid;
	mso-list-template-ids:330972744 68354051 68354051 68354053 68354049 68354051 68354053 68354049 68354051 68354053;}
@list l4:level1
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:36.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l4:level2
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:72.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l4:level3
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:108.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l4:level4
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:144.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l4:level5
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:180.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l4:level6
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:216.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l4:level7
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:252.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l4:level8
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:288.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l4:level9
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:324.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l5
	{mso-list-id:1027171825;
	mso-list-type:hybrid;
	mso-list-template-ids:739391388 68354051 68354051 68354053 68354049 68354051 68354053 68354049 68354051 68354053;}
@list l5:level1
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l5:level2
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l5:level3
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l5:level4
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l5:level5
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l5:level6
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l5:level7
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l5:level8
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l5:level9
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l6
	{mso-list-id:1129519328;
	mso-list-type:hybrid;
	mso-list-template-ids:337676782 68354049 68354051 68354053 68354049 68354051 68354053 68354049 68354051 68354053;}
@list l6:level1
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:36.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l6:level2
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:72.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l6:level3
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:108.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l6:level4
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:144.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l6:level5
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:180.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l6:level6
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:216.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l6:level7
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:252.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l6:level8
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:288.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l6:level9
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:324.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l7
	{mso-list-id:1268123591;
	mso-list-type:hybrid;
	mso-list-template-ids:696442284 68354049 68354051 68354053 68354049 68354051 68354053 68354049 68354051 68354053;}
@list l7:level1
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:36.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l7:level2
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:72.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l7:level3
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:108.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l7:level4
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:144.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l7:level5
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:180.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l7:level6
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:216.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l7:level7
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:252.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l7:level8
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:288.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l7:level9
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:324.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l8
	{mso-list-id:1483041707;
	mso-list-type:hybrid;
	mso-list-template-ids:-1578726124 68354051 68354051 68354053 68354049 68354051 68354053 68354049 68354051 68354053;}
@list l8:level1
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:36.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l8:level2
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:72.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l8:level3
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:108.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l8:level4
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:144.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l8:level5
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:180.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l8:level6
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:216.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l8:level7
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:252.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l8:level8
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:288.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l8:level9
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:324.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l9
	{mso-list-id:1864200872;
	mso-list-type:hybrid;
	mso-list-template-ids:-862812570 68354049 68354051 68354053 68354049 68354051 68354053 68354049 68354051 68354053;}
@list l9:level1
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:36.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l9:level2
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:72.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l9:level3
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:108.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l9:level4
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:144.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l9:level5
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:180.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l9:level6
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:216.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
@list l9:level7
	{mso-level-number-format:bullet;
	mso-level-text:\F0B7;
	mso-level-tab-stop:252.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Symbol;}
@list l9:level8
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:288.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:"Courier New";}
@list l9:level9
	{mso-level-number-format:bullet;
	mso-level-text:\F0A7;
	mso-level-tab-stop:324.0pt;
	mso-level-number-position:left;
	text-indent:-18.0pt;
	font-family:Wingdings;}
ol
	{margin-bottom:0cm;}
ul
	{margin-bottom:0cm;}
-->
</style>
<!--[if gte mso 10]>
<style>
 /* Style Definitions */
 table.MsoNormalTable
	{mso-style-name:Standaardtabel;
	mso-tstyle-rowband-size:0;
	mso-tstyle-colband-size:0;
	mso-style-noshow:yes;
	mso-style-unhide:no;
	mso-style-parent:"";
	mso-padding-alt:0cm 5.4pt 0cm 5.4pt;
	mso-para-margin:0cm;
	mso-pagination:widow-orphan;
	font-size:10.0pt;
	font-family:"Times New Roman",serif;}
</style>
<![endif]--><!--[if gte mso 9]><xml>
 <o:shapedefaults v:ext="edit" spidmax="1026"/>
</xml><![endif]--><!--[if gte mso 9]><xml>
 <o:shapelayout v:ext="edit">
  <o:idmap v:ext="edit" data="1"/>
 </o:shapelayout></xml><![endif]-->
</head>

<body lang=NL style='tab-interval:35.4pt;word-wrap:break-word'>

<div class=WordSection1>

<p class=Default><b>Voorbeeld vast contract <o:p></o:p></b></p>

<p class=Default><b><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></b></p>

<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>
"""

# Check if 'key' already exists in session_state
# If not, then initialize it
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Session State also supports the attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'
    
#from io import BytesIO
#from pyxlsb import open_workbook as open_xlsb
#import streamlit as st

#def to_file(html):
#    soup = BeautifulSoup(html, "html.parser") 
#    with open("output.html", "w+", encoding = 'utf-8') as file: 
#        file.write(str(soup.prettify()))
#    st.write("Je contract staat voor je klaar. Je kunt het in word openen, het bestand heet output")
#    return file


def expensive_process(option, bedrijfsnaam, vestigingsadres, postcode_en_plaats, voorletters_en_achternaam,voorletters_en_achternaam_werknemer, woonadres, postcode_en_plaats_werknemer, geboortedatum,datum, naam_functie, naam_cao, duur_proeftijd, type_dienstverband, aantal_uren, aantal_werkdagen_per_week, locatie_werkzaamheden,aantal_vakantie_dagen, aantal_vakantie_uren,naam_pensioenregeling, omschrijving_pensioenafspraken, plaatsnaam, datum_ondertekening):
    with st.spinner('Processing...'):
        time.sleep(5)
    html = basis_html + gegevens_werkgever(bedrijfsnaam, vestigingsadres, postcode_en_plaats, voorletters_en_achternaam)
    html += gegevens_werknemer(voorletters_en_achternaam_werknemer, woonadres, postcode_en_plaats_werknemer, geboortedatum)
    result = gegevens_arbeidsovereenkomst(datum, naam_functie, naam_cao)
    html += result[0]
    result = proeftijd(duur_proeftijd)
    html += result[0]
    html += werktijden_plaats(type_dienstverband, aantal_uren, aantal_werkdagen_per_week, locatie_werkzaamheden)
    result = vakantiedagen(aantal_vakantie_dagen, aantal_vakantie_uren)
    html += result[0]
    result = pensioen(naam_pensioenregeling, omschrijving_pensioenafspraken)
    html += result[0]
    html += opzegging_geheimhouding_ondertekening(plaatsnaam, datum_ondertekening)
    soup = BeautifulSoup(html, "html.parser")
    html = soup.prettify()
    # open the file in w mode 
    # set encoding to UTF-8 
    #file = to_file(html) #genereer het document
    return (html, bedrijfsnaam, vestigingsadres, postcode_en_plaats, voorletters_en_achternaam,voorletters_en_achternaam_werknemer, woonadres, postcode_en_plaats_werknemer, geboortedatum,datum, naam_functie, naam_cao, duur_proeftijd, type_dienstverband, aantal_uren, aantal_werkdagen_per_week, locatie_werkzaamheden,aantal_vakantie_dagen, aantal_vakantie_uren,naam_pensioenregeling, omschrijving_pensioenafspraken, plaatsnaam, datum_ondertekening)

def gegevens_werkgever(bedrijfsnaam, vestigingsadres, postcode_en_plaats, voorletters_en_achternaam):

    gegevens_werkgever = f"""<p class=Default><b><span style='font-size:10.0pt'>1 Gegevens werkgever </span></b><span
    style='font-size:10.0pt'><o:p></o:p></span></p>
    
    <p class=Default><span style='font-size:10.0pt'>Naam: {bedrijfsnaam};
    <o:p></o:p></span></p>
    
    <p class=Default><span style='font-size:10.0pt'>Adres: {vestigingsadres};
    <o:p></o:p></span></p>
    
    <p class=Default><span style='font-size:10.0pt'>{postcode_en_plaats};
    <o:p></o:p></span></p>
    
    <p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>
    
    <p class=Default><span style='font-size:10.0pt'>De werkgever wordt
    vertegenwoordigd door: <o:p></o:p></span></p>
    
    <p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>
    
    <p class=Default><span style='font-size:10.0pt'>Naam: {voorletters_en_achternaam}; <o:p></o:p></span></p>
    
    <p class=Default><span style='font-size:10.0pt'>Hierna te noemen de werkgever. <o:p></o:p></span></p>
    
    <p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>
    """ 
    
    return gegevens_werkgever

def gegevens_werknemer(voorletters_en_achternaam_werknemer, woonadres, postcode_en_plaats_werknemer, geboortedatum):
    gegevens_werknemer = f"""<p class=Default><b><span style='font-size:10.0pt'>2 Gegevens werknemer </span></b><span
style='font-size:10.0pt'><o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'>Naam: {voorletters_en_achternaam_werknemer}; <o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'>Adres: {woonadres};
<o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'>Postcode: {postcode_en_plaats_werknemer};
<o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'>Geboortedatum: {geboortedatum};
<o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>

<p class=Default><span style='font-size:10.0pt'>Hierna te noemen de werknemer. <o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>

<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>

<p class=Default><b><span style='font-size:10.0pt'>Werkgever en werknemer komen
het volgende overeen: </span></b><span style='font-size:10.0pt'><o:p></o:p></span></p>

<p class=Default><b><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></b></p>"""

    return gegevens_werknemer

def gegevens_arbeidsovereenkomst(datum, naam_functie, naam_cao):
    p = random.uniform(0,1) # er zijn twee opties, dus fifty-fifty keuze
    gegevens_arbeidsovereenkomst = f"""<p class=Default><b><span style='font-size:10.0pt'>3 Gegevens
arbeidsovereenkomst </span></b><span style='font-size:10.0pt'><o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'>De werknemer treedt op {datum};
</i>in dienst bij werkgever op basis van een arbeidsovereenkomst voor
onbepaalde tijd in de functie van {naam_functie}. <o:p></o:p></span></p>
<p class=Default><b><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></b></p>"""
    query_arbeidsovereenkomst = str(f"\ndatum in dienst: {datum}") + str(f"\nfunctietitel: {naam_functie}")
    
    if naam_cao == "":
        gegevens_arbeidsovereenkomst += """<p class=Default style='margin-left:36.0pt;text-indent:-18.0pt;mso-list:l5 level1 lfo6'><![if !supportLists]><span
style='font-size:10.0pt;font-family:"Courier New";mso-fareast-font-family:"Courier New"'><span
style='mso-list:Ignore'>o<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:10.0pt'>Op de
arbeidsovereenkomst is geen collectieve arbeidsovereenkomst (cao) van
toepassing. <o:p></o:p></span></p>
<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>"""
    else:
        gegevens_arbeidsovereenkomst += str(f"""<p class=Default style='margin-left:36.0pt;text-indent:-18.0pt;mso-list:l5 level1 lfo6'><![if !supportLists]><span
style='font-size:10.0pt;font-family:"Courier New";mso-fareast-font-family:"Courier New"'><span
style='mso-list:Ignore'>o<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:10.0pt'>Op de
arbeidsovereenkomst is de collectieve arbeidsovereenkomst (cao) {naam_cao} van toepassing. De werknemer ontvangt bij indiensttreding een
exemplaar van de cao. <o:p></o:p></span></p>
<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>""")
        query_arbeidsovereenkomst += str(f"\nnaam cao: {naam_cao}")
        

    return gegevens_arbeidsovereenkomst, query_arbeidsovereenkomst

def proeftijd(duur_proeftijd):
    p = random.uniform(0,1)
    proeftijd = """<p class=Default><b><span style='font-size:10.0pt'>4 Proeftijd </span></b><span
style='font-size:10.0pt'><o:p></o:p></span></p>
<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>"""
    if duur_proeftijd ==  '':
        proeftijd += """<p class=Default style='margin-left:36.0pt;text-indent:-18.0pt;mso-list:l4 level1 lfo7;
tab-stops:list 36.0pt'><![if !supportLists]><span style='font-size:10.0pt;
font-family:"Courier New";mso-fareast-font-family:"Courier New"'><span
style='mso-list:Ignore'>o<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:10.0pt'>Er is geen
proeftijd. <o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>
"""
        query_proeftijd = ""
    else:
        proeftijd += str(f"""<p class=Default style='margin-left:36.0pt;text-indent:-18.0pt;mso-list:l4 level1 lfo7;
tab-stops:list 36.0pt'><![if !supportLists]><span style='font-size:10.0pt;
font-family:"Courier New";mso-fareast-font-family:"Courier New"'><span
style='mso-list:Ignore'>o<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:10.0pt'>Er geldt een
proeftijd van {duur_proeftijd},
te rekenen vanaf het moment van indiensttreding. Tijdens de proeftijd kan de
arbeidsovereenkomst direct worden beëindigd door werkgever of werknemer. <o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>""")
        query_proeftijd = str(f"\nduratie proeftijd: {duur_proeftijd}")

    return proeftijd, query_proeftijd

def werktijden_plaats(type_dienstverband, aantal_uren, aantal_werkdagen_per_week, locatie_werkzaamheden):
    werktijden_plaats = f"""<p class=Default><b><span style='font-size:10.0pt'>5 Werktijden en plaats
werkzaamheden </span></b><span style='font-size:10.0pt'><o:p></o:p></span></p>
    <p class=Default><span style='font-size:10.0pt'>De werknemer werkt {type_dienstverband} voor {aantal_uren} uur per week. De werknemer werkt {aantal_werkdagen_per_week}. De werkzaamheden worden
gewoonlijk verricht {locatie_werkzaamheden}

<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>"""

    return werktijden_plaats

def loon_en_vakantietoeslag(bedrag_brutoloon, loonperiode):
    loon_en_vakantietoeslag = f"""<p class=Default><b><span style='font-size:10.0pt'>6 Loon en vakantietoeslag </span></b><span
style='font-size:10.0pt'><o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'>Het loon bedraagt {bedrag_brutoloon} bruto per {loonperiode}. Het loon wordt telkens
voor het einde van de loonbetalingsperiode uitbetaald. De vakantietoeslag
bedraagt 8% van het bruto jaarloon. Dit wordt naar evenredigheid van de duur
van de arbeidsovereenkomst opgebouwd in de periode van 1 juni tot en met 31
mei. De vakantietoeslag wordt uitbetaald in de maand juni. De werkgever
verstrekt per loonbetalingsperiode een loonspecificatie (loonstrook). <o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>"""

    return loon_en_vakantietoeslag

def vakantiedagen(aantal_vakantiedagen, aantal_vakantie_uren):
    p = random.uniform(0,1)
    vakantiedagen = """<p class=Default><b><span style='font-size:10.0pt'>7 Vakantiedagen </span></b><span
style='font-size:10.0pt'><o:p></o:p></span></p>
<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>"""
    if aantal_vakantiedagen != '':
        vakantiedagen += str(f"""<p class=Default style='margin-left:36.0pt;text-indent:-18.0pt;mso-list:l0 level1 lfo9;
tab-stops:list 36.0pt'><![if !supportLists]><span style='font-size:10.0pt;
font-family:"Courier New";mso-fareast-font-family:"Courier New"'><span
style='mso-list:Ignore'>o<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:10.0pt'>Werknemer heeft
recht op {aantal_vakantiedagen} vakantiedagen met behoud van loon per jaar. Deze
worden naar evenredigheid van de duur en de omvang van de arbeidsovereenkomst
opgebouwd. <o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>""")
        query_vakantiedagen = str(f"\naantal vakantiedagen: {aantal_vakantiedagen}")
    else:
        vakantiedagen += str(f"""<p class=Default><span style='font-size:10.0pt'>Werknemer heeft recht op {aantal_vakantie_uren} vakantie-uren met behoud van loon per jaar. Deze worden naar evenredigheid
van de duur en de omvang van de arbeidsovereenkomst opgebouwd. <o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>""")
        query_vakantiedagen = str(f"\naantal vakantie uren: {aantal_vakantie_uren}")

    return vakantiedagen, query_vakantiedagen
    
def pensioen(naam_pensioenregeling, omschrijving_pensioenafspraken):
    p = random.uniform(0,1)
    pensioen = """<p class=Default><b><span style='font-size:10.0pt'>8 Pensioen </span></b><span
style='font-size:10.0pt'><o:p></o:p></span></p>
<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>"""
    if naam_pensioenregeling == '' and omschrijving_pensioenafspraken == '':
        pensioen += str("""<p class=Default style='margin-left:36.0pt;text-indent:-18.0pt;mso-list:l1 level1 lfo8;
tab-stops:list 36.0pt'><![if !supportLists]><span style='font-size:10.0pt;
font-family:"Courier New";mso-fareast-font-family:"Courier New"'><span
style='mso-list:Ignore'>o<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:10.0pt'>Er is geen
verplichte pensioenregeling. <o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>""")
        query_pensioen = ""
    elif naam_pensioenregeling != '':
        pensioen += str(f"""<p class=Default style='margin-left:36.0pt;text-indent:-18.0pt;mso-list:l1 level1 lfo8;
tab-stops:list 36.0pt'><![if !supportLists]><span style='font-size:10.0pt;
font-family:"Courier New";mso-fareast-font-family:"Courier New"'><span
style='mso-list:Ignore'>o<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:10.0pt'>Werknemer valt
onder de verplichte pensioenregeling van {naam_pensioenregeling}.
Werkgever informeert werknemer over de inhoud en de toetredingsvoorwaarden van
het pensioen. <o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>""")
        query_pensioen = str(f"\nnaam pensioenregeling: {naam_pensioenregeling}")
    else: 
        pensioen += str(f"""<p class=Default style='margin-left:36.0pt;text-indent:-18.0pt;mso-list:l1 level1 lfo8;
tab-stops:list 36.0pt'><![if !supportLists]><span style='font-size:10.0pt;
font-family:"Courier New";mso-fareast-font-family:"Courier New"'><span
style='mso-list:Ignore'>o<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:10.0pt'>Werkgever en
werknemer spreken een vrijwillige pensioenregeling af. Deze houdt in {omschrijving_pensioenafspraken};. </i><o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>""")
        query_pensioen = str(f"\nomschrijving pensioenafspraken: {omschrijving_pensioenafspraken}")
    
    return pensioen, query_pensioen

def opzegging_geheimhouding_ondertekening(plaatsnaam, datum_ondertekening):
    tekst = f"""<p class=Default><b><span style='font-size:10.0pt'>9 Opzegging
arbeidsovereenkomst </span></b><span style='font-size:10.0pt'><o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'>Werknemer kan de
arbeidsovereenkomst opzeggen met inachtneming van een opzegtermijn van een
maand. Werkgever kan de arbeidsovereenkomst opzeggen met inachtneming van een
opzegtermijn van &#233&#233n maand. Als het dienstverband vijf jaar of langer duurt,
neemt werkgever de langere wettelijke opzegtermijn in acht. De opzegging gebeurt
tegen het einde van de maand. <o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>

<p class=Default><b><span style='font-size:10.0pt'>10 Geheimhouding </span></b><span
style='font-size:10.0pt'><o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'>De werknemer is verplicht tot
geheimhouding van alle gegevens over het bedrijf, de bedrijfsvoering en klanten
van de werkgever waarvan hij weet of redelijkerwijze kan vermoeden dat deze
vertrouwelijk zijn. Deze verplichting geldt ook na beëindiging van de
arbeidsovereenkomst. <o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>

<p class=Default><b><span style='font-size:10.0pt'>11 Ondertekening <o:p></o:p></span></b></p>

<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>

<p class=Default><span style='font-size:10.0pt'>Deze arbeidsovereenkomst is in
tweevoud opgemaakt. <o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>

<p class=Default><span style='font-size:10.0pt'>Plaats: {plaatsnaam};<span
style='mso-spacerun:yes'> </span><span style='mso-tab-count:2'> </span>Plaats:
{plaatsnaam}; <o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'>Datum: {datum_ondertekening}; <span style='mso-tab-count:1'> </span>Datum: {datum_ondertekening}; <o:p></o:p></span></p>

<p class=Default><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p>

<p class=Default><span style='font-size:10.0pt'>Handtekening werkgever <span
style='mso-tab-count:2'> </span>Handtekening werknemer <o:p></o:p></span></p>

<p class=MsoNormal><o:p>&nbsp;</o:p></p>"""
    
    return tekst 
    
st.title("Gegevensinvoer vast contract Certa advocaten")
# Miss in door het model te laten genereren tekst express de basis_html weglaten. dat scheelt echt mega veel namelijk. kun je dan later gewoon voor invoegen
#test_html = basis_html + gegevens_werkgever("InIn", "Julianaplein 33", "6942LO Den Bosch", "W.A.M. Mulders") + gegevens_werknemer("H.E.E. Hang", "Brandweer", "4614KN", "01-01-2001") + gegevens_arbeidsovereenkomst('01-01-2002', 'AI-engineer', 'IT-specialist') + proeftijd('7 maanden') + werktijden_plaats('fulltime', '40', '7 dagen per week', 'op kantoor in Den Bosch') + loon_en_vakantietoeslag('3000 euro', 'maand') + vakantiedagen('25', '200') +  pensioen("ABP", "je wordt rijk") + opzegging_geheimhouding_ondertekening('Den Bosch', '16-11-2023')


# Hier code opnemen om alle variables uit function random te genereren
queries = []
htmls = []

bedrijfsnaam = str(st.text_input("bedrijfsnaam"))#st.text_input("bedrijfsnaam")#input("Typ hier de bedrijfsnaam: ")
vestigingsadres= st.text_input("vestigingsadres")
postcode_en_plaats= st.text_input("postcode en plaats")
voorletters_en_achternaam= st.text_input("voorletters en achternaam vertegenwoordiger werkgever")


#html = basis_html + gegevens_werkgever(bedrijfsnaam, vestigingsadres, postcode_en_plaats, voorletters_en_achternaam) # ! voor uiteindelijke chatgpt input basis_html weghalen want scheelt veel tokens !!!
html = basis_html + gegevens_werkgever(bedrijfsnaam, vestigingsadres, postcode_en_plaats, voorletters_en_achternaam) # ! voor uiteindelijke chatgpt input basis_html weghalen want scheelt veel tokens !!!
    
voorletters_en_achternaam_werknemer = st.text_input("voorletters en achternaam werknemer") #st.text_input("Typ hier de voorletters en achternaam van de werknemer")#input("Typ hier de voorletters en achternaam van de werknemer: ")
woonadres = st.text_input("woonadres werknemer")
postcode_en_plaats_werknemer = st.text_input("postcode en plaats werknemer")
geboortedatum = st.text_input("geboortedatum werknemer")
    
html += gegevens_werknemer(voorletters_en_achternaam_werknemer, woonadres, postcode_en_plaats_werknemer, geboortedatum)
    
naam_functie = st.text_input("functietitel")
naam_cao = st.text_input("naam cao")
datum = st.text_input("datum ingang contract")
    

result = gegevens_arbeidsovereenkomst(datum, naam_functie, naam_cao)
html += result[0]

    
#proeftijd(duur_proeftijd)
duur_proeftijd = st.text_input("duratie proeftijd")
result = proeftijd(duur_proeftijd)

html += result[0]

type_dienstverband = st.text_input("type dienstverband")
aantal_uren = st.text_input("aantal uren per week")
aantal_werkdagen_per_week = st.text_input("aantal werkdagen per week")
locatie_werkzaamheden = st.text_input("locatie werkzaamheden")
    
html += werktijden_plaats(type_dienstverband, aantal_uren, aantal_werkdagen_per_week, locatie_werkzaamheden)
    #query += str(f"\ntype dienstverband: {type_dienstverband}") + str(f"\naantal uren: {aantal_uren}") + str(f"\naantal werkdagen per week: {aantal_werkdagen_per_week}") + str(f"\nlocatie werkzaamheden: {locatie_werkzaamheden}")
    

    
    #vakantiedagen(aantal_vakantie_dagen, aantal_vakantie_uren)
aantal_vakantie_dagen = st.text_input("aantal vakantie dagen (leeg i.g.v. uren)")
aantal_vakantie_uren = st.text_input("aantal vakantie uren (leeg i.g.v. dagen)")
    
result = vakantiedagen(aantal_vakantie_dagen, aantal_vakantie_uren)
html += result[0]
    #query += result[1]
    
#pensioen(naam_pensioenregeling, omschrijving_pensioenafspraken)
naam_pensioenregeling = st.text_input("naam pensioenregeling")
omschrijving_pensioenafspraken = st.text_input("omschrijving pensioenafspraken")
result = pensioen(naam_pensioenregeling, omschrijving_pensioenafspraken)
html += result[0]
    #query += result[1]
    
#opzegging_geheimhouding_ondertekening(plaatsnaam, datum_ondertekening)
plaatsnaam = st.text_input("plaatsnaam ondertekening")
datum_ondertekening = st.text_input("datum ondertekening")
html += opzegging_geheimhouding_ondertekening(plaatsnaam, datum_ondertekening)




cols = st.columns(2)
#option = cols[0].selectbox('Select a number', options=['1', '2', '3'])
#add = cols[1].number_input('Add a number', min_value=0, max_value=10)
#file_dl = to_file(html)
#[html, bedrijfsnaam, vestigingsadres, postcode_en_plaats, voorletters_en_achternaam,voorletters_en_achternaam_werknemer, woonadres, postcode_en_plaats_werknemer, geboortedatum,datum, naam_functie, naam_cao, duur_proeftijd, type_dienstverband, aantal_uren, aantal_werkdagen_per_week, locatie_werkzaamheden,aantal_vakantie_dagen, aantal_vakantie_uren,naam_pensioenregeling, omschrijving_pensioenafspraken, plaatsnaam, datum_ondertekening, file_dl] = expensive_process(option, bedrijfsnaam, vestigingsadres, postcode_en_plaats, voorletters_en_achternaam,voorletters_en_achternaam_werknemer, woonadres, postcode_en_plaats_werknemer, geboortedatum,datum, naam_functie, naam_cao, duur_proeftijd, type_dienstverband, aantal_uren, aantal_werkdagen_per_week, locatie_werkzaamheden,aantal_vakantie_dagen, aantal_vakantie_uren,naam_pensioenregeling, omschrijving_pensioenafspraken, plaatsnaam, datum_ondertekening)
#st.download_button(label='📥 Download Current Result',
#                                data=file_dl ,
#                                file_name= 'df_test.xlsx')

#docx = new_parser.parse_html_string(html)
#from htmldocx import HtmlToDocx

#new_parser = HtmlToDocx()
#new_parser.parse_html_file(input_html_file_path, output_docx_file_path)

# do more stuff to document
#document = Document()
#new_parser = HtmlToDocx()
#new_parser.add_html_to_document(html, document)
#document.save('htmlinword.docx')

#from docx import Document
#from html2docx import html2docx

#def html_to_docx(html_string, output_path):
    # Convert HTML to DOCX
#    html2docx(html_string, output_path)


# Output Word document path
#output_path = "htmlinword.docx"

# Convert HTML to DOCX
#html_to_docx(html, output_path)


st.download_button('Download arbeidsovereenkomst', html, file_name = "arbeidscontract.html")
#pdfgen.sync.from_string(html, 'out.pdf')
#pdfkit.from_string(html, 'out.pdf')
#with pdfplumber.open("out.pdf") as pdf:
#    st.download_button('Download arbeidsovereenkomst', pdf, file_name = "arbeidscontract.pdf")

if 'processed' not in st.session_state:
    st.session_state.processed = {}

# Process and save results
#if st.button('Process'):
#    result = expensive_process(option, bedrijfsnaam, vestigingsadres, postcode_en_plaats, voorletters_en_achternaam,voorletters_en_achternaam_werknemer, woonadres, postcode_en_plaats_werknemer, geboortedatum,datum, naam_functie, naam_cao, duur_proeftijd, type_dienstverband, aantal_uren, aantal_werkdagen_per_week, locatie_werkzaamheden,aantal_vakantie_dagen, aantal_vakantie_uren,naam_pensioenregeling, omschrijving_pensioenafspraken, plaatsnaam, datum_ondertekening)
#    st.session_state.processed[option] = result

#if option in st.session_state.processed:
#    st.write(f'Option {option} processed with add {bedrijfsnaam}')
#    st.write(st.session_state.processed[option][0])
