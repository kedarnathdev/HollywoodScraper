import requests
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout


class ScrollViewExample(ScrollView):
    pass

class BoxLayoutExample(BoxLayout):
    my_text = StringProperty("")
    my_text2 = StringProperty("")
    searchq = StringProperty("")
    inter_select = StringProperty("1")
    final_result = StringProperty("")

    def on_button_click(self):
        print("Button Clicked")
        self.change_label(self.ids.movie_search)

    def change_label(self, widget):
        self.my_text = widget.text
        self.my_text2 = widget.text
        self.hollywood_search(widget.text)

    def change_label2(self, widget):
        self.inter_select = widget.text
    def on_button_inter_click(self):
        self.change_label2(self.ids.movie_inter_search)
        self.hollywood_final()

    def hollywood_search(self, searchq):

        #searchq = input("Enter a movie name: ")
        qs = {
            "limit": 50,
            "query_term": searchq
        }
        page = "https://yts.mx/api/v2/list_movies.json"

        r = requests.get(page, params=qs)
        r_dict = r.json()
        movie_list = []
        for i in range(r_dict['data']['movie_count']):
            print(f"{i + 1}){r_dict['data']['movies'][i]['title_long']}")
            movie_list.append(r_dict['data']['movies'][i]['id'])
        b = [f"{i + 1}){r_dict['data']['movies'][i]['title_long']}" for i in range(r_dict['data']['movie_count'])]

        self.my_text = "No. of movies found: " + str(r_dict['data']['movie_count']) +"\n"

        for i in range(len(b)):
            self.my_text = self.my_text + str(b[i]) + "\n"


    def hollywood_final(self):

        qs = {
            "limit": 50,
            "query_term": self.my_text2
        }
        page = "https://yts.mx/api/v2/list_movies.json"

        r = requests.get(page, params=qs)
        r_dict = r.json()
        movie_list = []
        for i in range(r_dict['data']['movie_count']):
            movie_list.append(r_dict['data']['movies'][i]['id'])
        for j in range(len(movie_list)):
            if int(str(self.inter_select)) - 1 == j:
                page2 = "https://yts.mx/api/v2/movie_details.json"
                page2_params = {
                    "movie_id": movie_list[j]
                }
                mov_api = requests.get(page2, params=page2_params)
                mov_api_dict = mov_api.json()

                self.final_result = "Your Selection:-" + "\n" + "Movie Name: " + mov_api_dict['data']['movie'][
                    'title_long'] + "\n" + "IMDB rating: " + str(mov_api_dict['data']['movie'][
                        'rating']) + "/10" + "\n" + "Duration: " + str(
                    mov_api_dict['data']['movie']['runtime']) + " minutes" + "\n" + "Total no. of downloads: " + str(
                    mov_api_dict['data']['movie']['download_count']) + "\n"+ "\n"

                e = [mov_api_dict['data']['movie']['torrents'][i]['quality'] for i in range(len(mov_api_dict['data']['movie']['torrents']))]
                for i in range(len(e)):
                    if mov_api_dict['data']['movie']['torrents'][i]['quality'] == '3D':
                        self.final_result = self.final_result + "3D Torrent link:- "+"\n" + "link: " + str(mov_api_dict['data']['movie']['torrents'][i]['url'])+"\n" + "size: " + str(mov_api_dict['data']['movie']['torrents'][i]['size'])+"\n" + "seeds/peers:" + str(mov_api_dict['data']['movie']['torrents'][i]['seeds']) +"/"+ str(mov_api_dict['data']['movie']['torrents'][i]['peers'])+ "(more no. of seeds = good speed)"+"\n"+"\n"
                    if mov_api_dict['data']['movie']['torrents'][i]['quality'] == '2160p':
                        self.final_result = self.final_result + "4K(2160p) Torrent link:- "+"\n" + "link: " + str(mov_api_dict['data']['movie']['torrents'][i]['url'])+"\n" + "size: " + str(mov_api_dict['data']['movie']['torrents'][i]['size'])+"\n" + "seeds/peers:" + str(mov_api_dict['data']['movie']['torrents'][i]['seeds']) +"/"+ str(mov_api_dict['data']['movie']['torrents'][i]['peers'])+ "(more no. of seeds = good speed)"+"\n"+"\n"
                    if mov_api_dict['data']['movie']['torrents'][i]['quality'] == '1080p':
                        self.final_result = self.final_result + "FHD(1080p) Torrent link:- "+"\n" + "link: " + str(mov_api_dict['data']['movie']['torrents'][i]['url'])+"\n" + "size: " + str(mov_api_dict['data']['movie']['torrents'][i]['size'])+"\n" + "seeds/peers:" + str(mov_api_dict['data']['movie']['torrents'][i]['seeds']) +"/"+ str(mov_api_dict['data']['movie']['torrents'][i]['peers'])+ "(more no. of seeds = good speed)"+"\n"+"\n"
                    if mov_api_dict['data']['movie']['torrents'][i]['quality'] == '720p':
                        self.final_result = self.final_result + "HD(720p) Torrent link:- "+"\n" + "link: " + str(mov_api_dict['data']['movie']['torrents'][i]['url'])+"\n" + "size: " + str(mov_api_dict['data']['movie']['torrents'][i]['size'])+"\n" + "seeds/peers:" + str(mov_api_dict['data']['movie']['torrents'][i]['seeds']) +"/"+ str(mov_api_dict['data']['movie']['torrents'][i]['peers'])+ "(more no. of seeds = good speed)"+"\n"+"\n"



class HollyWoodGUI(App):
    pass

HollyWoodGUI().run()