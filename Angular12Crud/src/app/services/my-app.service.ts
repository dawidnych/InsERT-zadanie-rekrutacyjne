import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Category } from '../models/category.model';
import { Offers } from '../models/offers.model';

const baseUrlCategory = 'http://localhost:8080/category';
const baseUrlOffers = 'http://localhost:8080/offers';

@Injectable({
  providedIn: 'root'
})

export class CategoryService {

  constructor(private http: HttpClient) { }

  getAll(): Observable<Category[]> {
    return this.http.get<Category[]>(baseUrlCategory);
  }

  get(id: any): Observable<Category> {
    return this.http.get(`${baseUrlCategory}/${id}/`);
  }

  create(data: any): Observable<any> {
    return this.http.post(baseUrlCategory, data);
  }

  update(id: any, data: any): Observable<any> {
    return this.http.put(`${baseUrlCategory}/${id}/`, data);
  }

  delete(id: any): Observable<any> {
    return this.http.delete(`${baseUrlCategory}/${id}/`);
  }

  deleteAll(): Observable<any> {
    return this.http.delete(baseUrlCategory);
  }
}

export class OffersService {

  constructor(private http: HttpClient) { }

  getAll(): Observable<Offers[]> {
    return this.http.get<Offers[]>(baseUrlOffers);
  }

  get(id: any): Observable<Offers> {
    return this.http.get(`${baseUrlOffers}/${id}/`);
  }

  create(data: any): Observable<any> {
    return this.http.post(baseUrlOffers, data);
  }

  update(id: any, data: any): Observable<any> {
    return this.http.put(`${baseUrlOffers}/${id}/`, data);
  }

  delete(id: any): Observable<any> {
    return this.http.delete(`${baseUrlOffers}/${id}/`);
  }

  deleteAll(): Observable<any> {
    return this.http.delete(baseUrlOffers);
  }
}
