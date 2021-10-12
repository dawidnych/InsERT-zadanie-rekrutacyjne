import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CategoryListComponent} from "./components/category-list/category-list.component";
import { CategoryDetailsComponent} from "./components/category-details/category-details.component";
import { AddCategoryComponent} from "./components/add-category/add-category.component";
import { OffersListComponent} from "./components/offers-list/offers-list.component";
import { OfferDetailsComponent} from "./components/offer-details/offer-details.component";
import { AddOfferComponent} from "./components/add-offer/add-offer.component";

const routes: Routes = [
  { path: '', redirectTo: 'category', pathMatch: 'full' },
  { path: 'category', component: CategoryListComponent },
  { path: 'category/:id/', component: CategoryDetailsComponent },
  { path: 'category', component: AddCategoryComponent },
  { path: 'offers', component: OffersListComponent },
  { path: 'offers/:id/', component: OfferDetailsComponent },
  { path: 'offers', component: AddOfferComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
