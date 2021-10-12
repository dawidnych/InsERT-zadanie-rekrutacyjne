import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AddCategoryComponent } from './components/add-category/add-category.component';
import { AddOfferComponent } from './components/add-offer/add-offer.component';
import { CategoryDetailsComponent } from './components/category-details/category-details.component';
import { OfferDetailsComponent } from './components/offer-details/offer-details.component';
import { OffersListComponent } from './components/offers-list/offers-list.component';
import { CategoryListComponent } from './components/category-list/category-list.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    AddCategoryComponent,
    AddOfferComponent,
    CategoryDetailsComponent,
    OfferDetailsComponent,
    OffersListComponent,
    CategoryListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
