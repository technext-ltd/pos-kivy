import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
import json
import os
from datetime import datetime

Builder.load_string('''
<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15
        
        Label:
            text: 'POS System'
            font_size: '28sp'
            bold: True
            size_hint_y: 0.15
            color: 0.2, 0.6, 0.8, 1
            
        Button:
            text: '📦 Product Input'
            font_size: '20sp'
            background_color: 0.2, 0.6, 0.8, 1
            background_normal: ''
            size_hint_y: 0.2
            on_press: root.manager.current = 'product_input'
            
        Button:
            text: '📱 Product Scanner'
            font_size: '20sp'
            background_color: 0.3, 0.7, 0.5, 1
            background_normal: ''
            size_hint_y: 0.2
            on_press: root.manager.current = 'product_scanner'
            
        Button:
            text: '👥 Customer Viewer'
            font_size: '20sp'
            background_color: 0.8, 0.6, 0.2, 1
            background_normal: ''
            size_hint_y: 0.2
            on_press: root.manager.current = 'customer_viewer'
            
        Button:
            text: '❌ Exit'
            font_size: '20sp'
            background_color: 0.8, 0.3, 0.3, 1
            background_normal: ''
            size_hint_y: 0.15
            on_press: app.stop()

<ProductInputScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15
        
        Label:
            text: '📦 Product Input'
            font_size: '24sp'
            bold: True
            size_hint_y: 0.1
            color: 0.2, 0.6, 0.8, 1
            
        BoxLayout:
            orientation: 'vertical'
            spacing: 10
            size_hint_y: 0.7
            
            BoxLayout:
                orientation: 'horizontal'
                size_hint_y: 0.2
                Label:
                    text: 'Product Code:'
                    font_size: '18sp'
                    color: 0.2, 0.2, 0.2, 1
                    size_hint_x: 0.4
                TextInput:
                    id: code_input
                    multiline: False
                    font_size: '18sp'
                    hint_text: 'Enter product code'
                    size_hint_x: 0.6
                    
            BoxLayout:
                orientation: 'horizontal'
                size_hint_y: 0.2
                Label:
                    text: 'Product Name:'
                    font_size: '18sp'
                    color: 0.2, 0.2, 0.2, 1
                    size_hint_x: 0.4
                TextInput:
                    id: name_input
                    multiline: False
                    font_size: '18sp'
                    hint_text: 'Enter product name'
                    size_hint_x: 0.6
                    
            BoxLayout:
                orientation: 'horizontal'
                size_hint_y: 0.2
                Label:
                    text: 'Price:'
                    font_size: '18sp'
                    color: 0.2, 0.2, 0.2, 1
                    size_hint_x: 0.4
                TextInput:
                    id: price_input
                    multiline: False
                    font_size: '18sp'
                    hint_text: 'Enter price'
                    input_filter: 'float'
                    size_hint_x: 0.6
                
        BoxLayout:
            orientation: 'horizontal'
            spacing: 10
            size_hint_y: 0.15
            
            Button:
                text: '💾 Save'
                font_size: '18sp'
                background_color: 0.2, 0.8, 0.2, 1
                background_normal: ''
                on_press: root.save_product()
                
            Button:
                text: '🧹 Clear'
                font_size: '18sp'
                background_color: 0.8, 0.8, 0.2, 1
                background_normal: ''
                on_press: root.clear_fields()
                
        BoxLayout:
            orientation: 'horizontal'
            spacing: 10
            size_hint_y: 0.15
            
            Button:
                text: '📋 View Products'
                font_size: '18sp'
                background_color: 0.6, 0.2, 0.8, 1
                background_normal: ''
                on_press: root.view_products()
                
            Button:
                text: '⬅️ Back'
                font_size: '18sp'
                background_color: 0.8, 0.2, 0.2, 1
                background_normal: ''
                on_press: root.manager.current = 'main'

<ProductScannerScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        
        Label:
            text: '📱 Product Scanner'
            font_size: '24sp'
            bold: True
            size_hint_y: 0.06
            color: 0.3, 0.7, 0.5, 1
            
        BoxLayout:
            orientation: 'vertical'
            spacing: 5
            size_hint_y: 0.25
            
            Label:
                text: '🔍 Search Products:'
                font_size: '14sp'
                color: 0.2, 0.2, 0.2, 1
                size_hint_y: 0.2
                
            TextInput:
                id: search_input
                multiline: False
                font_size: '14sp'
                hint_text: 'Type product name to search...'
                size_hint_y: 0.3
                on_text: root.search_products()
                
            ScrollView:
                size_hint_y: 0.5
                GridLayout:
                    id: search_results
                    cols: 1
                    size_hint_y: None
                    height: self.minimum_height
                    spacing: 2
                    
        BoxLayout:
            orientation: 'vertical'
            spacing: 5
            size_hint_y: 0.35
            
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: 0.3
                Label:
                    text: 'Customer:'
                    font_size: '14sp'
                    color: 0.2, 0.2, 0.2, 1
                    size_hint_y: 0.3
                TextInput:
                    id: customer_input
                    multiline: False
                    font_size: '14sp'
                    hint_text: 'Enter customer name'
                    size_hint_y: 0.7
                    on_text: root.search_customers()
                
            ScrollView:
                size_hint_y: 0.2
                GridLayout:
                    id: customer_results
                    cols: 1
                    size_hint_y: None
                    height: self.minimum_height
                    spacing: 1
                    
            BoxLayout:
                orientation: 'horizontal'
                size_hint_y: 0.25
                Label:
                    text: 'Product Code:'
                    font_size: '14sp'
                    color: 0.2, 0.2, 0.2, 1
                    size_hint_x: 0.3
                TextInput:
                    id: scan_input
                    multiline: False
                    font_size: '14sp'
                    hint_text: 'Enter product code'
                    size_hint_x: 0.7
                    on_text_validate: root.scan_product()
                    
            BoxLayout:
                orientation: 'horizontal'
                size_hint_y: 0.25
                Label:
                    text: 'Quantity:'
                    font_size: '14sp'
                    color: 0.2, 0.2, 0.2, 1
                    size_hint_x: 0.3
                TextInput:
                    id: quantity_input
                    multiline: False
                    font_size: '14sp'
                    text: '1'
                    input_filter: 'int'
                    size_hint_x: 0.7
                    
        Label:
            id: current_total
            text: 'Total: $0.00'
            font_size: '16sp'
            bold: True
            color: 0.2, 0.5, 0.2, 1
            size_hint_y: 0.04
                
        ScrollView:
            size_hint_y: 0.2
            Label:
                id: product_info
                text: 'Scanned products will appear here'
                font_size: '12sp'
                text_size: self.width, None
                size_hint_y: None
                height: self.texture_size[1]
                color: 0.2, 0.2, 0.2, 1
                
        BoxLayout:
            orientation: 'horizontal'
            spacing: 5
            size_hint_y: 0.05
            
            Button:
                text: '📥 Scan'
                font_size: '14sp'
                background_color: 0.2, 0.8, 0.2, 1
                background_normal: ''
                on_press: root.scan_product()
                
            Button:
                text: '❌ Remove Last'
                font_size: '14sp'
                background_color: 0.8, 0.6, 0.2, 1
                background_normal: ''
                on_press: root.remove_last()
                
        BoxLayout:
            orientation: 'horizontal'
            spacing: 5
            size_hint_y: 0.05
            
            Button:
                text: '💰 Complete Sale'
                font_size: '14sp'
                background_color: 0.2, 0.6, 0.8, 1
                background_normal: ''
                on_press: root.complete_sale()
                
            Button:
                text: '⬅️ Back'
                font_size: '14sp'
                background_color: 0.8, 0.2, 0.2, 1
                background_normal: ''
                on_press: root.manager.current = 'main'

<CustomerViewerScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        
        Label:
            text: '👥 Customer Viewer'
            font_size: '24sp'
            bold: True
            size_hint_y: 0.08
            color: 0.8, 0.6, 0.2, 1
            
        BoxLayout:
            orientation: 'horizontal'
            spacing: 10
            size_hint_y: 0.08
            
            Label:
                text: 'Customer:'
                font_size: '16sp'
                color: 0.2, 0.2, 0.2, 1
                size_hint_x: 0.3
                
            Spinner:
                id: customer_spinner
                text: 'Select Customer'
                font_size: '16sp'
                size_hint_x: 0.7
                on_text: root.load_customer_data()
                
        ScrollView:
            size_hint_y: 0.84
            GridLayout:
                id: customer_data_container
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                spacing: 5
                padding: 5
                
        BoxLayout:
            orientation: 'horizontal'
            spacing: 10
            size_hint_y: 0.08
            
            Button:
                text: '🔄 Refresh'
                font_size: '16sp'
                background_color: 0.2, 0.8, 0.2, 1
                background_normal: ''
                on_press: root.refresh_customers()
                
            Button:
                text: '⬅️ Back'
                font_size: '16sp'
                background_color: 0.8, 0.2, 0.2, 1
                background_normal: ''
                on_press: root.manager.current = 'main'
''')

# Utility functions for file operations
def load_json_file(filename, default_value):
    """Safely load JSON file, return default value if error occurs"""
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                data = json.load(f)
                if isinstance(data, dict):
                    return data
                else:
                    return default_value.copy()
        else:
            return default_value.copy()
    except Exception as e:
        return default_value.copy()

def save_json_file(filename, data):
    """Safely save data to JSON file"""
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        return False

# Screens
class MainScreen(Screen):
    pass

class ProductInputScreen(Screen):
    PRODUCTS_FILE = 'products.json'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ensure_products_file()
    
    def ensure_products_file(self):
        if not os.path.exists(self.PRODUCTS_FILE):
            save_json_file(self.PRODUCTS_FILE, {})
    
    def save_product(self):
        code = self.ids.code_input.text.strip()
        name = self.ids.name_input.text.strip()
        price_text = self.ids.price_input.text.strip()
        
        if not code or not name or not price_text:
            self.show_popup('❌ Error', 'Please fill all fields!')
            return
        
        try:
            price = float(price_text)
            if price <= 0:
                raise ValueError("Price must be positive")
        except ValueError:
            self.show_popup('❌ Error', 'Please enter a valid price!')
            return
        
        products = load_json_file(self.PRODUCTS_FILE, {})
        
        if code in products:
            self.show_popup('❌ Error', 'Product code already exists!')
            return
        
        products[code] = {
            'name': name,
            'price': price
        }
        
        if save_json_file(self.PRODUCTS_FILE, products):
            self.show_popup('✅ Success', f'Product "{name}" saved successfully!')
            self.clear_fields()
        else:
            self.show_popup('❌ Error', 'Failed to save product!')
    
    def clear_fields(self):
        self.ids.code_input.text = ''
        self.ids.name_input.text = ''
        self.ids.price_input.text = ''
    
    def view_products(self):
        products = load_json_file(self.PRODUCTS_FILE, {})
        
        if not products:
            self.show_popup('📦 Products', 'No products found!')
            return
        
        product_list = "📦 Product List:\n\n"
        for code, product in products.items():
            product_list += f"Code: {code}\nName: {product['name']}\nPrice: ${product['price']:.2f}\n{'-'*30}\n"
        
        self.show_popup('📦 Products', product_list)
    
    def show_popup(self, title, message):
        content = Label(text=message, font_size='16sp')
        content.bind(texture_size=lambda *x: setattr(content, 'size', content.texture_size))
        
        popup = Popup(title=title,
                     content=content,
                     size_hint=(0.9, 0.8))
        popup.open()

class ProductScannerScreen(Screen):
    PRODUCTS_FILE = 'products.json'
    CUSTOMERS_FILE = 'customers.json'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_items = []
        self.ensure_files()
    
    def ensure_files(self):
        if not os.path.exists(self.PRODUCTS_FILE):
            save_json_file(self.PRODUCTS_FILE, {})
        if not os.path.exists(self.CUSTOMERS_FILE):
            save_json_file(self.CUSTOMERS_FILE, {})
    
    def search_products(self):
        search_term = self.ids.search_input.text.strip().lower()
        search_layout = self.ids.search_results
        search_layout.clear_widgets()
        
        if not search_term:
            return
        
        products = load_json_file(self.PRODUCTS_FILE, {})
        found_products = []
        
        for code, product in products.items():
            if search_term in product['name'].lower():
                found_products.append((code, product))
        
        # Show max 8 results
        for code, product in found_products[:8]:
            # Create search result button with better layout
            btn = Button(size_hint_y=None, height=60)
            btn.background_color = (0.95, 0.95, 0.95, 1)
            btn.background_normal = ''
            
            # Main layout
            main_layout = BoxLayout(orientation='vertical', padding=5, spacing=2)
            
            # Product name and code row
            name_layout = BoxLayout(orientation='horizontal', size_hint_y=0.6)
            name_label = Label(text=product['name'], font_size='14sp', 
                             color=(0.2, 0.2, 0.2, 1), halign='left',
                             text_size=(None, None))
            code_label = Label(text=f"Code: {code}", font_size='12sp',
                             color=(0.5, 0.5, 0.5, 1), halign='right',
                             text_size=(None, None))
            name_layout.add_widget(name_label)
            name_layout.add_widget(code_label)
            
            # Price row
            price_layout = BoxLayout(orientation='horizontal', size_hint_y=0.4)
            price_label = Label(text=f"Price: ${product['price']:.2f}", 
                              font_size='13sp', color=(0.2, 0.5, 0.2, 1),
                              halign='left', text_size=(None, None))
            price_layout.add_widget(price_label)
            
            main_layout.add_widget(name_layout)
            main_layout.add_widget(price_layout)
            btn.add_widget(main_layout)
            
            # Bind the click event
            btn.bind(on_press=lambda instance, code=code: self.select_search_result(code))
            search_layout.add_widget(btn)
    
    def search_customers(self):
        search_term = self.ids.customer_input.text.strip().lower()
        customer_layout = self.ids.customer_results
        customer_layout.clear_widgets()
        
        if not search_term:
            return
        
        customers = load_json_file(self.CUSTOMERS_FILE, {})
        found_customers = []
        
        for customer_name in customers.keys():
            if search_term in customer_name.lower():
                found_customers.append(customer_name)
        
        # Show max 5 customer results
        for customer_name in found_customers[:5]:
            btn = Button(text=customer_name, size_hint_y=None, height=40,
                        font_size='12sp', background_color=(0.9, 0.95, 0.9, 1),
                        background_normal='')
            btn.bind(on_press=lambda instance, name=customer_name: self.select_customer(name))
            customer_layout.add_widget(btn)
    
    def select_customer(self, customer_name):
        self.ids.customer_input.text = customer_name
        self.ids.customer_results.clear_widgets()
        self.ids.scan_input.focus = True
    
    def select_search_result(self, product_code):
        self.ids.scan_input.text = product_code
        self.ids.search_input.text = ''
        self.ids.search_results.clear_widgets()
        self.ids.quantity_input.focus = True
    
    def scan_product(self):
        code = self.ids.scan_input.text.strip()
        customer = self.ids.customer_input.text.strip()
        quantity_text = self.ids.quantity_input.text.strip()
        
        if not customer:
            self.show_popup('❌ Error', 'Please enter customer name!')
            return
        
        if not code:
            self.show_popup('❌ Error', 'Please enter product code!')
            return
        
        try:
            quantity = int(quantity_text)
            if quantity <= 0:
                raise ValueError("Quantity must be positive")
        except ValueError:
            self.show_popup('❌ Error', 'Please enter a valid quantity!')
            return
        
        products = load_json_file(self.PRODUCTS_FILE, {})
        
        if code not in products:
            self.show_popup('❌ Error', 'Product code not found!')
            return
        
        product = products[code]
        total_price = product['price'] * quantity
        
        self.current_items.append({
            'code': code,
            'name': product['name'],
            'price': product['price'],
            'quantity': quantity,
            'total': total_price
        })
        
        self.update_display()
        self.ids.scan_input.text = ''
        self.ids.quantity_input.text = '1'
        self.ids.customer_results.clear_widgets()
    
    def remove_last(self):
        if self.current_items:
            self.current_items.pop()
            self.update_display()
        else:
            self.show_popup('ℹ️ Info', 'No items to remove!')
    
    def update_display(self):
        if not self.current_items:
            self.ids.product_info.text = 'No products scanned yet'
            self.ids.current_total.text = 'Total: $0.00'
            return
        
        display_text = '🛒 Current Items:\n\n'
        grand_total = 0
        
        for i, item in enumerate(self.current_items, 1):
            display_text += f"{i}. {item['name']} x{item['quantity']}: ${item['total']:.2f}\n"
            grand_total += item['total']
        
        display_text += f"\n💵 Grand Total: ${grand_total:.2f}"
        self.ids.product_info.text = display_text
        self.ids.current_total.text = f'Total: ${grand_total:.2f}'
    
    def complete_sale(self):
        if not self.current_items:
            self.show_popup('❌ Error', 'No products to sell!')
            return
        
        customer = self.ids.customer_input.text.strip()
        if not customer:
            self.show_popup('❌ Error', 'Please enter customer name!')
            return
        
        total = sum(item['total'] for item in self.current_items)
        customers = load_json_file(self.CUSTOMERS_FILE, {})
        
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        if customer not in customers:
            customers[customer] = {}
        
        if current_date not in customers[customer]:
            customers[customer][current_date] = []
        
        customers[customer][current_date].extend(self.current_items)
        
        if save_json_file(self.CUSTOMERS_FILE, customers):
            self.show_popup('✅ Success', f'Sale completed!\\nCustomer: {customer}\\nTotal: ${total:.2f}\\nItems: {len(self.current_items)}')
            self.current_items = []
            self.update_display()
            self.ids.customer_input.text = ''
            self.ids.search_results.clear_widgets()
            self.ids.customer_results.clear_widgets()
        else:
            self.show_popup('❌ Error', 'Failed to save sale!')
    
    def show_popup(self, title, message):
        popup = Popup(title=title,
                     content=Label(text=message, font_size='18sp'),
                     size_hint=(0.8, 0.5))
        popup.open()

class CustomerViewerScreen(Screen):
    CUSTOMERS_FILE = 'customers.json'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.customers_data = {}
        Clock.schedule_once(self.refresh_customers, 0.1)
    
    def refresh_customers(self, *args):
        self.customers_data = load_json_file(self.CUSTOMERS_FILE, {})
        
        spinner = self.ids.customer_spinner
        customer_names = sorted(self.customers_data.keys())
        
        if customer_names:
            spinner.values = ['Select Customer'] + customer_names
        else:
            spinner.values = ['Select Customer']
        
        spinner.text = 'Select Customer'
        self.load_customer_data()
    
    def load_customer_data(self):
        customer = self.ids.customer_spinner.text
        container = self.ids.customer_data_container
        container.clear_widgets()
        
        if customer == 'Select Customer' or customer not in self.customers_data:
            label = Label(text='Select a customer to view their purchase history', 
                         font_size='16sp', color=(0.5, 0.5, 0.5, 1),
                         size_hint_y=None, height=100)
            container.add_widget(label)
            return
        
        customer_info = self.customers_data[customer]
        
        if not customer_info:
            label = Label(text='No purchases found for this customer', 
                         font_size='16sp', color=(0.5, 0.5, 0.5, 1),
                         size_hint_y=None, height=100)
            container.add_widget(label)
            return
        
        # Add customer header
        header = BoxLayout(orientation='horizontal', size_hint_y=None, height=60)
        header_label = Label(text=f'👤 {customer}', font_size='20sp', bold=True, 
                           color=(0.2, 0.4, 0.6, 1))
        header.add_widget(header_label)
        container.add_widget(header)
        
        # Sort dates in descending order
        sorted_dates = sorted(customer_info.keys(), reverse=True)
        lifetime_total = 0
        total_transactions = len(sorted_dates)
        
        for date in sorted_dates:
            transaction_total = 0
            items = customer_info[date]
            
            # Create purchase history card
            card = BoxLayout(orientation='vertical', size_hint_y=None, height=140, 
                           padding=10, spacing=5)
            card.background_color = (0.95, 0.95, 0.95, 1)
            
            # Date header
            date_label = Label(text=f"📅 {date}", font_size='16sp', bold=True,
                             color=(0.2, 0.4, 0.6, 1), size_hint_y=0.2,
                             text_size=(None, None))
            card.add_widget(date_label)
            
            # Items list
            items_text = ""
            for item in items:
                items_text += f"• {item['name']} x{item['quantity']}: ${item['total']:.2f}\\n"
                transaction_total += item['total']
            
            items_label = Label(text=items_text, font_size='12sp',
                              color=(0.3, 0.3, 0.3, 1), size_hint_y=0.6,
                              text_size=(None, None))
            card.add_widget(items_label)
            
            # Transaction summary
            summary = BoxLayout(orientation='horizontal', size_hint_y=0.2)
            total_label = Label(text=f"Total: ${transaction_total:.2f}", 
                              font_size='14sp', bold=True, color=(0.2, 0.6, 0.2, 1))
            items_count = Label(text=f"{len(items)} items", 
                              font_size='12sp', color=(0.5, 0.5, 0.5, 1))
            summary.add_widget(total_label)
            summary.add_widget(items_count)
            card.add_widget(summary)
            
            container.add_widget(card)
            lifetime_total += transaction_total
        
        # Add lifetime summary
        summary_card = BoxLayout(orientation='vertical', size_hint_y=None, height=80,
                               padding=10, spacing=5)
        summary_card.background_color = (0.9, 0.95, 0.9, 1)
        
        lifetime_label = Label(text=f'🏆 Lifetime Total: ${lifetime_total:.2f}', 
                             font_size='18sp', bold=True, color=(0.2, 0.6, 0.2, 1))
        transactions_label = Label(text=f'📊 Total Transactions: {total_transactions}', 
                                 font_size='14sp', color=(0.5, 0.5, 0.5, 1))
        
        summary_card.add_widget(lifetime_label)
        summary_card.add_widget(transactions_label)
        container.add_widget(summary_card)

# Main App
class POSApp(App):
    def build(self):
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        sm = ScreenManager()
        
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(ProductInputScreen(name='product_input'))
        sm.add_widget(ProductScannerScreen(name='product_scanner'))
        sm.add_widget(CustomerViewerScreen(name='customer_viewer'))
        
        return sm

if __name__ == '__main__':
    POSApp().run()